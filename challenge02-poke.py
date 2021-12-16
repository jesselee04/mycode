#!/usr/bin/env python3

print("Welcome to the PokeAPI data parser")

# dataSet is JSON adapted from https://PokeAPI.co
dataSet = [{"ability": {"name": "static", "attack type": "electric"}, "is_hidden": False, "slot":1}, {"ability": {"name": "Lightning-rod", "attack type": "electric"}, "is_hidden": True, "slot":3}]

# Finish the code below this line
# -------------------------------

# use a for loop to display all the abilities
for i in dataSet:
    print(i)

print()

# display JUST the details of a single abilities
for i in dataSet:
    print(i.get("ability"))

print()

# display JUST the names of a single ability
for i in dataSet:
    print(i.get("ability").get("name"))
