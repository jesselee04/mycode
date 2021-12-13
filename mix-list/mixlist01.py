#!/usr/bin/env python3

# Create my list
my_list = [ "192.168.0.5", 5060, "UP" ]

# Print the IP Address from the list
print("The first item in the list (IP): " + my_list[0] )

# Print the port number from the list
print("The second item in the list (port): " + str(my_list[1]) )

# Print the state from the list
print("The last item in the list (state): " + my_list[2] )


# Create my iplist
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# Print only the IP Address from the list
print(f"The ip addresses listed are: {iplist[3]} and {iplist[4]}" )

