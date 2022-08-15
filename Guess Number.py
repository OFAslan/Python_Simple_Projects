"""With this code computer get a secret number and we tried to guess it."""

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    trials = 0
    while guess != random_number:
        trials += 1
        guess = int(input(f"Guess a number betweeen 1 and {x} \
        "))
        if guess < random_number:
            print("Make a new guess a little bit higher")
        elif guess > random_number:
            print("Make a guess a little bit lower")
        
    print(f"Yaaay, congrats. You have guessed the correct number {random_number}")
    print(f"You have found the correct number in {trials} times of trial.")
    

guess(10)