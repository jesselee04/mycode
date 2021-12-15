#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #indent to keep the dns file object open
    #loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n')
        # remove new line character if exists would exist on all but last line
        # if the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as svrfile:
                svrfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as svrfile:
                svrfile.write(svr + "\n")


