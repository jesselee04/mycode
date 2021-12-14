#!/usr/bin/env python3

# Counter
round = 0

#Loop
while True:

    # round counter
    round = round + 1

    # question to user
    print('Finish the movie title, "Monty Python\'s The Life of ______"')

    # answer
    answer = input("Your guess--> ")

    #Check to see if answer is right
    if answer == 'Brian':
        print('Correct')

        break

    elif round==3:
        print("Sorry, the answer was Brian.")

        break

    else:
        print("Sorry! Try again!")


