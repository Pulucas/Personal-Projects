# https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/
# colored output: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
# colored output cheatsheet: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
import json
from random import randint as rand

green = "\33[32m"
blue = "\33[34m"
white = "\33[37m"
reset = "\33[0m"


def main():
    print("Welcome to Wordle!")
    print(blue + "Blue is correct letter in wrong position." + reset)
    print(green + "Green is correct letter in correct position." + reset)
    print(white + "White means the letter is not in the word." + reset)
    totalGuesses = 0
    usedLetters = set()
    guess = askInput()
    while guess != word:
        tempChars = set()

        for char in guess:
            if char in usedLetters:
                tempChars.add(char)

        if len(tempChars) != 0:
            print("You used letters:", tempChars)
            print("You cannot use letters:", usedLetters)
            tempChars = []
            guess = askInput()
            continue

        for char in guess:
            if char not in word:
                usedLetters.add(char)

        printColors(guess)
        totalGuesses += 1
        guess = askInput()
    printColors(guess)
    print(f"It took you {totalGuesses + 1} guesses.")


def askInput():
    guess = input("guess: ").lower()

    while len(guess) != 5 or guess not in fullWordlist:
        if len(guess) != 5:
            print("You must input a 5 letter word.")
            guess = input("guess: ").lower()
            continue
        if guess not in fullWordlist:
            print("You must input a real word.")
            guess = input("guess: ").lower()
            continue

    return guess


def colorChar(word, char, index):
    if word[index] == char:
        return green + char + reset
    elif char in word:
        return blue + char + reset
    else:
        return white + char + reset


def printColors(guess):
    print(colorChar(word, guess[0], 0), colorChar(word, guess[1], 1), colorChar(
        word, guess[2], 2), colorChar(word, guess[3], 3), colorChar(word, guess[4], 4))


with open("./wordlist.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    allowedWordlist = data["allowedWordlist"]
    fullWordlist = data["fullWordlist"]

word = allowedWordlist[rand(0, len(allowedWordlist) - 1)]

main()
