#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

#print out the entire list
print(proto)

#add on "dns"
proto.append("dns")
protoa.append("dns")

#print updated proto list
print(proto)


proto2 = [ 22, 80, 443, 53 ]

#extend proto with proto 2 list
proto.extend(proto2)

#print updated proto list
print(proto)

#append protoa with proto 2
protoa.append(proto2)

#print updated protoa list
print(protoa)

#test insert
proto.insert(0,"insert1")

print(proto)

#test2
proto.insert(3,"insert2")

print(proto)
