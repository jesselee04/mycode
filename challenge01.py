#!/usr/bin/env python3


"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------

# Print out the Names of the munsters
print("The names of the munsters are: " + str(munsters['names']))

input("Press Enter to continue...")

# Print out the End date of the show
print("The end date of munsters was: " + str(munsters['endDate']))

input("Press Enter to continue...")

# Print out the Start date of the show
print("The start date of munsters was: " + str(munsters['startDate']))

input("Press Enter to continue...")

# Add number of episodes to the dictionary
munsters['Episodes'] = '70'

# Print out the number of episodes for the show
print("There were " + str(munsters['Episodes']) + " episodes in the series.")
