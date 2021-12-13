#!/usr/bin/env python3

animal_list = ["Fox", "Ant", "Bee"]
animal_list2 = ["cod", "cow", "hot"]

print(animal_list)

print(animal_list2)

animal_list.append(animal_list2)
print(animal_list)

animal_list.extend(animal_list2)
print(animal_list)
