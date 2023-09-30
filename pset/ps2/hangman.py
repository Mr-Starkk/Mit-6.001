# Problem Set 2, hangman.py
# Name: Yash
# Collaborators: NaN
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    bool = True
    for char in secret_word:
        if char not in letters_guessed:
            bool = False
    return bool

#print(is_word_guessed('apple', ['l', 'i', 'e', 'p', 'r', 'a']))
        


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    # temp = list(secret_word) #converts string secret_word to a list
    output = [] #an empty list of same length as secret_word and all characters '_ '
    i=0
    while i < len(secret_word):
        output.append('_ ')
        i += 1
    #loop that indexes over temp and copies the index to output if a character matches 
    for char in letters_guessed:
                i = 0
                while i < len(secret_word):
                    if secret_word[i] == char:
                        output[i] = char
                    i += 1
    return ''.join(output)

# print(get_guessed_word('apple', ['e','i','k','p','r','s']) )


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_not_guessed = list(string.ascii_lowercase)
    for char in letters_guessed:
        if char in letters_not_guessed:
            letters_not_guessed.remove(char)
    return ''.join(letters_not_guessed)

# print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))



# def hangman(secret_word):
#     '''
#     secret_word: string, the secret word to guess.
    
#     Starts up an interactive game of Hangman.
    
#     * At the start of the game, let the user know how many 
#       letters the secret_word contains and how many guesses s/he starts with.
      
#     * The user should start with 6 guesses

#     * Before each round, you should display to the user how many guesses
#       s/he has left and the letters that the user has not yet guessed.
    
#     * Ask the user to supply one guess per round. Remember to make
#       sure that the user puts in a letter!
    
#     * The user should receive feedback immediately after each guess 
#       about whether their guess appears in the computer's word.

#     * After each guess, you should display to the user the 
#       partially guessed word so far.
    
#     Follows the other limitations detailed in the problem write-up.
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     no_of_guess = 6 #user starts with 6 guesses
#     warnings = 3 #and 3 warnings
#     letters_guessed = []
#     i = 0
#     unique_letters = []
#     for char in secret_word:
#         if char not in unique_letters:
#             unique_letters += char
            
#     print("Welcome to the game Hangman! \nI am thinking of a word that is", len(secret_word), "letters long. \nYou have", warnings, "warnings left.\n ------------------")
        
#     while is_word_guessed(secret_word, letters_guessed) == False and no_of_guess > 0 :
#         print("You have", no_of_guess, "guesses left")
#         print("Available letters:", get_available_letters(letters_guessed))
#         letters_guessed += input("Please guess a letter:")
#         #if letter already guessed, show warning/deduct no of guesses
#         if letters_guessed[-1] in letters_guessed[0:-1]: 
#                 if warnings < 1:
#                     no_of_guess -= 1
#                     print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
#                 else:
#                     warnings -= 1
#                     print("Oops! You've already guessed that letter. You have", warnings," warnings left:")
#         elif letters_guessed[i] in secret_word:
#             print("Good guess:")
#         elif letters_guessed[i] in string.ascii_letters:
#             no_of_guess -= 1
#             print("Oops! That letter is not in my word:")
#         else:
#             if warnings < 1:
#                 no_of_guess -= 1
#                 print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:")
#             else:
#                 warnings -= 1
#                 print("Oops! That is not a valid letter. You have", warnings," warnings left:")
#         i+=1
#         print(get_guessed_word(secret_word, letters_guessed),'\n\n------------------')
    
#     if is_word_guessed(secret_word, letters_guessed):
#         print("Good guess:", secret_word, '\n ------------------')
#         print("Congratulations, you won! \nYour total score for this game is:", no_of_guess*len(unique_letters))
#     else:
#         print("Sorry, you ran out of guesses. The word was", secret_word )
    
    
    
    
# # secret_word = "else"
# hangman(choose_word(wordlist))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #removes spaces form my_word
    my_word = my_word.replace(' ', '')
    
    #return false if the lengths are different
    if len(my_word) != len(other_word):
        return False
    
    #continue if the letter is an underscore and return false if the
    #letters dont match
    for i in range(len(my_word)):
        if my_word[i] == "_":
            continue
        elif my_word[i] != other_word[i]:
            return False
        
    #returns true if lengths are same and all corresponding letters match/are underscores    
    return True
            

# print(match_with_gaps('_ _ _ _ ', 'else'))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)
    if len(matched_words)> 0:
        print(' '.join(matched_words))
    else:
        print("No matches found")
            
# show_possible_matches("abbbbbb_ ")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    no_of_guess = 6 #user starts with 6 guesses
    warnings = 3 #and 3 warnings
    letters_guessed = []
    i = 0
    unique_letters = []
    for char in secret_word:
        if char not in unique_letters:
            unique_letters += char
            
    print("Welcome to the game Hangman! \nI am thinking of a word that is", len(secret_word), "letters long. \nYou have", warnings, "warnings left.\n ------------------")
        
    while is_word_guessed(secret_word, letters_guessed) == False and no_of_guess > 0 :
        print("You have", no_of_guess, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        letter_entered = input("Please guess a letter:")
        if letter_entered == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed += letter_entered
            #if letter already guessed, show warning/deduct no of guesses
            if letters_guessed[-1] in letters_guessed[0:-1]: 
                    if warnings < 1:
                        no_of_guess -= 1
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
                    else:
                        warnings -= 1
                        print("Oops! You've already guessed that letter. You have", warnings," warnings left:")
            elif letters_guessed[i] in secret_word:
                print("Good guess:")
            elif letters_guessed[i] in string.ascii_letters:
                no_of_guess -= 1
                print("Oops! That letter is not in my word:")
            else:
                if warnings < 1:
                    no_of_guess -= 1
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:")
                else:
                    warnings -= 1
                    print("Oops! That is not a valid letter. You have", warnings," warnings left:")
            i+=1
            print(get_guessed_word(secret_word, letters_guessed),'\n\n------------------')
    
    if is_word_guessed(secret_word, letters_guessed):
        print("Good guess:", secret_word, '\n ------------------')
        print("Congratulations, you won! \nYour total score for this game is:", no_of_guess*len(unique_letters))
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word )
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
# #     # pass

# #     # To test part 2, comment out the pass line above and
# #     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

# ##############
    
#     To test part 3 re-comment out the above lines and 
#     uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
