# to create a number guessing game

import random
target = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == target:
    print("Correct!")
else:
    print(f"Wrong! The number was {target}")