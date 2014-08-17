import subprocess
import socket
import re


def main():

    reqchk()


def ipcollect():
  # this function collects the internal ip's to install nimbus on.
  # *add later* use the ip addresses to confirm hostnames via /etc/hosts

    valid = []
    invalid = []

    x = raw_input("internal ip's to install Nimbus on [space seperated]: ")

  # uses spaces to split input and performs basic checks to confirm accuracy
    splitx = x.split()

    for splitip in splitx:
        try:
            socket.inet_aton(splitip)
        except socket.error:
            invalid.append(splitip)
        else:
            valid.append(splitip)
    return (valid)


def reqchk():
  # instantiate list from ipcollect function and write to a dsh group
    ips = ipcollect()
    reqchk_group = open('/etc/dsh/group/reqchk', 'w')
    for ip in ips:
        reqchk_group.write(ip)
        reqchk_group.write("\n")
    reqchk_group.close()

  # confirm required files exist on each host
    doiexist = ["/root/.rackspace/server_number",
                "/root/.rackspace/datacenter",
                "/root/.rackspace/customer_number"]

    for ip in ips:
        loopcnt = 0
        for path in doiexist:
            gather = subprocess.call(["ssh", ip, "cat " + path])
            re.sub(r'^0', '\n', str(gather))
            loopcnt += 1

            if loopcnt == 3:
                print "---"


if __name__ == "__main__":
    main()
