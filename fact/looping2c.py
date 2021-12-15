#!/usr/bin/env python3

# Open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
        #indent to keep the dnsfile object open
        #loop across the lines in the file
        for svr in dnsfile:
            print(svr, end="")

