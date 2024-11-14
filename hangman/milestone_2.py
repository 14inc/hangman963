import random

word_list = ['apple', 'kiwi', 'orange', 'pear', 'plum']

print(word_list)

for _ in range(5):
    word = random.choice(word_list)
    print(word)

guess = input("Please enter a single letter...\n")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
