#!/usr/bin/python3
import socket
import random
import sys

#SOCKET INFORMATION
target = "challenges.ctfd.io"
port = 30075
maxbuffer = 4096
# CONNECT TO SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port))
# WHILE THE CONNECTION IS UP

# available letters to try out
letters = 'abcdefghijklmnopqrstuvwxyz'

while True:
    data = s.recv(maxbuffer).decode()
    print(data)
    # the server is asking for a word
    if "Your guess?" in data:
        pass

    #server provides me letters 'abcdefghijklmnopqrstuvwxyz'

    # count how many '_' in the word is

    # if the word length is the # of '_',

    # for each letter in vowels:

        # select one random vowel and send to the server

    # if the letter is correct, the number of '_'s will decrease by 1.

    # if th letter is incorrect, the number of '_'s will not decrease by 1.

    # if i get 'Invalid! The word was innumerable.' in data, sys.exit(1)


