#!/usr/bin/python3
import socket

# CREATE A VOWELS LIST/TUPLE TO STORE THEM FOR FUTURE REMOVAL FROM THE STRINGS
vowels = ('a','e','i','o','u','-', ' ', '>')
# DESIGNATE TARGET AND PORT FOR SOCKET
target = "challenges.ctfd.io"
port = 30070
MAXBUFFER = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = s.connect((target, port))
# INITIATE THE CONNECTION TO THE REMOTE SOCKET

# WHILE THE SOCKET CONNECTION IS UP,
while True:
# READ THE RESPONSE FROM THE SERVER
    data = s.recv(MAXBUFFER).decode()
    print(f"Word: {data}")
# IF THE RESPONSE SAYS 'NO VOWELS FOR YOU'
    if "No vowels for you!\n" in data:
# SPLIT IT AT THE LINE BREAK \N AND REMOVE IT, LEAVING THE STRING AND '->'
        str1 = data.split("\n")[1]
        #print(str1)
# IF THE STRIPPED DOWN STRING CONTAINS VOWELS, REMOVE THE VOWELS, '->' AND WHITESPACE AND SAVE THE WORD TO A VARIABLE
        for chars in str1:
            if chars in vowels:
                str1 = str1.replace(chars, "")
        print(f"Voweless: {str1}\n")
        s.sendall(str1.encode())
    elif "->" in data:
        #print(f"i see something interesting")
        str2 = data.split("->")[0]
        #print(str2)
        for chars in str2:
            if chars in vowels:
                str2 = str2.replace(chars, "")
        print(f"Voweless: {str2}\n")
        s.sendall(str2.encode())
    else:
        break
        




