#!/usr/bin/env python3

## import module
import re

## regex for ip
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

## function for ip validation
def check(ipchk):
    if(re.search(regex, ipchk)):
        print("Looks like the IP address was set: " + ipchk)
    else:
        print("Invalid IP")

if __name__ == '__main__' :

    ## get ip address
    ipchk = input("Apply an IP Address: ")

    ## calling function
#    check(ipchk)

    

    ##if user set IP Of gateway
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    elif ipchk:
        check(ipchk)






