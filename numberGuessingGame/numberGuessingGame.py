# https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/
from random import random as rand

num = int(rand() * 100)  # Random interger between 1 and 100

# Asks for number and returns an integer


def askInput():
    userInput = input("Guess the number between 1 and 100: ")
    while not userInput.isdigit():  # If the user's input is not an integer, then ask for a number
        userInput = input("Guess the number between 1 and 100: ")
    return int(userInput)


userInput = askInput()
while userInput != num:
    if userInput > num:
        print("You number was too high")
        userInput = askInput()
    else:
        print("Your number was too low")
        userInput = askInput()

print("Your guessed the correct number!")
