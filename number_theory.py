#!/usr/bin/python3
import socket
import string

#SOCKET INFORMATION
target = "challenges.ctfd.io"
port = 30072
maxbuffer = 4096

# CONNECT TO SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port))

while True:
    data = s.recv(maxbuffer).decode()
    print(data)
    if "What is" in data:
        # what is num1 added/subtacted/multipled/divided num2?
        #strip out numbers and the operator, minus, plus, multiplied by, 
        data = data.split()
        # specify numbers variable with all digits
        digitz = string.digits
        # for every character in the data response

        # create an empty list to hold the numbers to assign them to variables in the future
        charList = []
        for char in data:
            # for every number digit
            for x in digitz:
                # if the strings in the data start with a number
                if char.startswith(x):
                    # remove other stuff from the numbers
                    char = char.replace("?", "")
                    char = char.replace("\n", "")
                    charList.append(char)
                    #print(charList)
                    # save the numbers each to its own variable number1 and number2
                    #number1, number2 = char
        #print(charList)
    # assign the numbers in the list to their own variables
        number1 = int(charList[0])
        number2 = int(charList[1])        
        if "plus" in data:
            answer = number1 + number2
            print(f"{answer} \n")
        elif "minus" in data:
            answer = number1 - number2
            print(f"{answer} \n")
        elif "multiplied" in data:
            answer = number1 * number2
            print(f"{answer} \n")
        elif "divided" in data:
            answer = number1 / number2
            print(f"{answer} \n")
        answer = str(answer)
        # SEND THE ANSWER BACK TO THE SERVER
        s.send(answer.encode())
    else:
        break