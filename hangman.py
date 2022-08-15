from words_list import words
import random
import string
import time

def get_valid_word(any_word_list):
    word = random.choice(any_word_list) #randomly chooses a word from the list.
    while "-" in word or " " in word:
        word = random.choice(any_word_list)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word.
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed.
    
    lives = 6
    
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        print("You have", lives, "lives left and you have used these letters:", " ".join(used_letters))
        
        #what the current word is (for example: W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        time.sleep(0.3)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 #we took a life
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print("You have already used this character, please try again.")
        
        else:
            print("Invalid chracter, please enter a correct letter.")
    
    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:    
        print("You guessed the",word, "correctly !!")
    
hangman()