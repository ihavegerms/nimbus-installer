#!/usr/bin/python

import socket
import string
import sys
import os

def main():
    reqchk()
    ipcollect()

def ipcollect():

    # this function collects the internal ip's to install nimbus on.
    # *add later* use the ip addresses to confirm hostnames via /etc/hosts

    valid = []
    invalid = []

    cont = raw_input("internal ip address of your Controller node: ")
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

    print (valid, invalid)

def reqchk():
    # this function first confirms the required data files are in place for nimbus install
    # basic checks are performed to confirm accuracy... there may be a better way to do it,
    # so modify later if needed... [germs - aug-14-14]
    test1 = os.path.isfile("/root/.rackspace/server_number")
    test2 = os.path.isfile("/root/.rackspace/datacenter")
    test3 = os.path.isfile("/root/.rackspace/customer_number")

    if test1 and test2 and test3 is True:
        pass
    elif test1 is False:
        print "[error] /root/.rackspace/server_number is missing"
        srvnum = raw_input("please enter the server_number: ")
        if len(srvnum) < 10 and srvnum.isdigit():
            srvnumfi = open('/root/.rackspace/server_number', 'w')
            srvnumfi.write(srvnum)
            srvnumfi.close()
            reqchk()
        else:
            print "The server number entered is invalid."
            reqchk()
    elif test2 is False:
        print "[error] /root/.rackspace/datacenter is missing"
        datacen = raw_input("please enter the datacenter: ")
        if len(datacen) < 4 and datacen.isidgit() == False:
            datacenfi = open('/root/.rackspace/datacenter', 'w')
            datacentfi.write(datacen)
            datacentfi.close()
            reqchk()
        else:
            print "The datacenter entered is invalid."
            reqchk()
    elif test3 is False:
        print "[error] /root/.rackspace/customer_number is missing"
        custnum = raw_input("please enter the account number: ")
        if len(custnum) < 10 and custnum.isdigit():
            custnumfi = open('/root/.rackspace/customer_number', 'w')
            custnumfi.write(custnum)
            custnumfi.close()
            reqchk()
        else:
            print "The customer number entered is invalid."
            reqchk()

if __name__ == "__main__":
    main()
