import random

class Hangman:
    '''
    This class is used to represent a hangman game.

    Attributes:
        word(str): The word to be guessed, picked randomly from the word_list.
        word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed.
        num_letters(int): The number of UNIQUE letters in the word that have not been guessed yet.
        num_lives(int): The number of lives the player has at the start of the game.
        word_list(list): A list of words.
        list_of_guesses(list): A list of the guesses that have already been tried.
    '''

    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This method checks if the letter entered by the user is in the word to be guessed.

        Args:
            guess(str): the letter guessed by the user

        Returns:
            None
        '''
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in list(enumerate(self.word)):
                if letter == guess:
                    self.word_guessed[index] = letter

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This method will ask the user to guess a letter that should be in the word.

        Args:
            None

        Returns:
            None
        '''
        while True:
            guess = input("Guess a letter...\n")
            
            if len(guess) != 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    '''
        This function will moderate the Hangman game that is being played by the user.

        Args:
            word_list: A list of possible words that the computer will randomly choose from.

        Returns:
            None
    '''
    num_lives = 5

    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
           # print("num of letters")
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")

word_list = ['apple', 'kiwi', 'orange', 'pear', 'plum']
play_game(word_list)