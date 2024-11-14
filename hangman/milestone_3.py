import random


def check_guess(guess):
    word_list = ['apple', 'kiwi', 'orange', 'pear', 'plum']
    secret_word = random.choice(word_list)
    
    guess = guess.lower()

    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter...\n")
        
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

ask_for_input()