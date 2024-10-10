import random
from words import word_list
import string

def get_valid_word(word_list):
    word = random.choice(word_list)

    while '-' in word or ' ' in word:
        word = random.choice(word_list)

    return word

def hangman():
    word = get_valid_word(word_list)
    word = word.upper()
    word_letters = set(word) # letters in the word
    aplphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has already used

    # getting user input
    while len(word_letters) > 0:
        print('\nYou have used this letters: ', ' '.join(used_letters))

        current_guess = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(current_guess))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in aplphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        
        else:
            print('Invalid character. Please try again.')

        if len(word_letters) == 0:
            print("\nCongratulations! You guessed the word:\n" + word)


hangman()

