import subprocess
import socket
import re

x = raw_input("internal ip's to install Nimbus on [space seperated]: ")

def main():

    reqchk()


def ipcollect():
  # this function collects the internal ip's to install nimbus on.
  # *add later* use the ip addresses to confirm hostnames via /etc/hosts
    global x
    valid = []
    invalid = []

  # uses spaces to split input and performs basic checks to confirm accuracy
    splitx = x.split()

    for splitip in splitx:
        try:
            socket.inet_aton(splitip)
        except socket.error:
            invalid.append(splitip)
        else:
            valid.append(splitip)
    return valid


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

    proceed = raw_input("Is the above information correct (y/n): ")
    print ""
    if proceed.lower() == "y":
        print "[+] proceeding with installation..."
        install()
    elif proceed.lower() == "n":
        print "[-] exiting per request..."
        exit

def install():

    ips = ipcollect()
    print "[+] downloading/extracting/installing nimbus-installer.tar.gz"
    for ip in ips:
        subprocess.call(["wget", "--quiet", "http://nimbus.howopenstack.org/nimbus-installer.tar.gz",
                         "-O", "/tmp/nimbus-installer.tar.gz"])
        subprocess.call(["wget", "--quiet", "--no-check-certificate",
                         "https://raw.githubusercontent.com/rcbops/support-tools/master/support-scripts/rax-nimbus-installer.sh",
                         "-qO", "/tmp/rax-nimbus-installer.sh"])
        subprocess.call(["bash", "/tmp/rax-nimbus-installer.sh"])
    print '[+] installation complete. verify openstack probes' \
          ' in /opt/nimsoft/probes/'
    print "[+] this process could take up to 15 minutes"
    print ""

if __name__ == "__main__":
    main()
