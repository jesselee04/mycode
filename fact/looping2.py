#!/usr/bin/env python3

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create list of lines
dnslist = dnsfile.readlines()

# loop over lines
for srv in dnslist:
    #print and end without a new line
    print(srv, end="")

#close the file
dnsfile.close()
