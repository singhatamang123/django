import time
import random

name = input("Enter your name: ")
print("Hi," + name, "Time to play game")
time.sleep(1)
print("Processing game...")
time.sleep(0.5)
words = ['programming', 'math', 'science', 'developer', 'coding', 'sester', 'software']
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("\nEnter a character:")
    guesses += guess
    if guess not in word:
        turns -=1
        print("\nwrong")
        print("\nYou have", + turns, 'more guesses')
        if turns ==0:
            print('\nYou lose')