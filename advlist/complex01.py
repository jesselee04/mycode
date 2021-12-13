#!/usr/bin/env python3

def main():
    #create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    #display list1
    print(list1)

    #display list[1] which should display arista_eos
    print(list1[1])

    #create list2
    list2 = ["juniper"]

    #extend list1 by list2 together
    list1.extend(list2)

    #display list 1, with jupiter
    print(list1)

    #create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #use the append operation to append list1 by list3
    list1.append(list3)

    #display the new complex list
    print(list1)

    #display the list of ip addresses
    print(list1[4])

    #display the first ip address
    print(list1[4][0])
main()
