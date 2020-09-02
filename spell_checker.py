#!/usr/bin/python3

# Read in the words file and create a dictionary
mydict = {} # word --> True
suggester = {} sorted_word --> [word1, word2, word3, word4]
# that maps lowercased word --> True; the keys will be the words and values will be true/false.
with open("words", 'r') as in_file:
    for line in in_file:
        word = line.strip().lower()
        mydict[word] = True # the word is the 'key' for the dictionary
    

# ask the user for some text (ideally, a word)
user_input = input("Enter a word here: ")

# While we have some text from the user
while user_input:

    # clean it up a bit: lowercase the text, remove any whitespace
    user_input = user_input.strip().lower()

    # take the cleaned up text, and see if it's in the dictionary
    if user_input in mydict:
    
        # if it is, tell the user that the word is good to go
        print("Yes, that's a word!")

        # if it's not, tell the user it's not a word
    elif user_input not in mydict:
        pass

    else:

        print("Nope, not a word!")

    # ask for more text from the user
    user_input = input("Gimme another word: ")
