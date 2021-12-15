#!/usr/bin/env python3

# Create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]

# Create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

# Loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended")
