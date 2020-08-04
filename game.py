"""This game is made by me Sudhanshu Naik (@_innocentson_).
In this game you have to choose a number and a random number will chosen by cpu. Your chosen number has to be matched with cpu chosen number then you will be the winner.
BELIEVE ME!!! YOU CANNOT WIN THIS GAME VERY EASILY.

Thank you and love you all."""

# Import Random Library
import random

# Let user try to enter a number between 1 and 100 to get the answer.
user = int(input("enter a number: "))

# Let random library choose a number between 1 and 100.
cpu = random.randint(0,100)

# Find whether user chosen number and random library chosen number matches or not.
if user > 0:
    if user == cpu:
        print('Congratulations!!! Your chosen number {} matches CPU chosen number {}.'.format(user,cpu))
    elif user > cpu:
        print('Oh!!! Your chosen number {} is more than CPU chosen number {}.'.format(user,cpu))
    elif user < cpu:
        print('Oh!!! Your chosen number {} is less than CPU chosen number {}.'.format(user,cpu))
else:
    print("Don\'t take 0 man.")