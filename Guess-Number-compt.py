"""With this code we will have a secret number and computer will guess it"""

import random

def computer_guess(x):
    low = 0
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could be high because high = low
        feedback = input(f"Is {guess} to high (H), too low (L) or correct (C)??  ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        #we don't put another condition for "c" because "c" will break the loop so we put its output out of the loop as below.
    print(f"Yayyy! The computer guessed your number {guess} correctly")
    
computer_guess(10)
            