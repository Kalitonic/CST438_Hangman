# Pooja Subramanian

# web based hangman game where all processing and game content 
# will be handled and delivered by an http server program.

# import necessary libs
import csv           # for importing words list
import random
import numpy as np   # for unique

# import word list csv into a list
word_list = []                  # empty list

with open('./words.csv') as w:  # import words list 
    reader = csv.reader(w)
    for row in reader:          # read words list into word_list
        for i in row:
            word_list.append(i)

# global values
word = ''     # empty string to eventually hold word
letter = ''   # right guess variable holder
guesses = ''  # holds guessed letters
guess = None  # None type to eventually hold current guess

class Game():
    
    def getWord():                                        # randomly pick a word from word list
        for n in range(len(word_list)):
            num = random.randint(0,len(word_list)-1)      # run random, get random num in range
        word = word_list[num]
        return word
    
    def display(letter, word, guesses):
        word = word.upper()
        blank = '_' * len(word)                            # display blanks
        guesses = guesses.upper()
        
        print("Guesses: ", guesses, end=' ')
        print('\n')
        
        for l in range(len(word)):                         # replace blanks if correct letter 
            if word[l] in letter:
                blank = blank[:l] + word[l] + blank[l+1:]  # update blanks
        
        for l in blank:
            print(l, end=' ')
    
    def guessed(guesses):
        guess = input('\nGuess a letter: ')
        guess = guess.upper()                              # standardize input to uppercase
        if len(guess) != 1:
            print('No more than 1 input.')
        elif guess in guesses:
            print('Already guessed.')
        elif guess.isalpha() == False:
            print('Not in alphabet.')
        else:
            return guess
    
    def runGame(letter, word, guesses, guess):
        word = Game.getWord()
        while len(guesses) <= 6:
            Game.display(letter, word, guesses)
            guess = Game.guessed(guesses)
            while guess == None:                         # check if guess is None type, cycle until not
                guess = Game.guessed(guesses)
            if guess in word.upper():
                if guess in letter:
                    print('Already guessed.')
                    continue
                else:
                    letter = letter + guess
            else:
                guesses = guesses + guess
            if len(letter) == len(np.unique(list(word))): # break loop for win condition
                break

        if len(letter) == len(np.unique(list(word))):    # double check win condition
            Game.display(letter, word, guesses)
            print("\nYou win!")

        elif len(guesses) <= 7:                          # check loss condition
            Game.display(letter, word, guesses)
            print("\nHangman!")
            print("The word was", word.upper())

Game.runGame(letter, word, guesses, guess)