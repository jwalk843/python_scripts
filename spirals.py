#!/usr/bin/python3
import socket

#SOCKET INFORMATION
target = "challenges.ctfd.io"
port = 30082
maxbuffer = 4096

# CONNECT TO SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port))

# DEFINE FIBONACCI FUNCTION TO GET US THE NUMBER
def getFibonnaci(num): 
    usermax = num
    counter = 0 # changing this from 1 to 0
    left_hand = 0
    right_hand = 1
    while not counter > usermax:
        # Create a dictionary of [key] counter: [value] left_hand
        fibo_dictionary = dict(FN=left_hand)
        #print(fibo_dictionary)
        # for every 
        #print(f"#{counter} = {left_hand}")
        #COUNTER AND LEFTHAND WILL BE KEY:VALUE PAIR IN DICTIONARY
        #fibdict = list(counter, left_hand)
        desk = left_hand + right_hand
        left_hand = right_hand
        right_hand = desk
        counter += 1
        # get the value for the sequence str1 key variable
        thevalue = fibo_dictionary
        for v in thevalue.values():
            #print(f"{counter}: {v}")
            if counter == num:
                answer = f"{v}".strip()
                return answer

# STRIP DATA FROM THE SERVER'S RESPONSE, LEAVING ONLY THE NUMBER ITS ASKING FOR
def stripChars(data):
    #data_split = data.split(".")[5].split(" ")[3].strip("").split(" ")  # this prints 176th for example
    #data_split = data_split[0]
    for x in data:
        if not x.isdigit():
            data = data.replace(x, "")
            data_noLetters = data[2::]
    return data_noLetters

while True:
    data = s.recv(maxbuffer).decode()
    print(data)
    # if it sees 'fibonacci number' in the string, strip it out
    if "->" not in data:
        num = stripChars(data)
        num = num.strip()
        num = int(num)
        print(f"Stripped data: {num}")
        fibo = getFibonnaci(num)
        print(fibo)
        s.sendall(fibo.encode())
    elif "->" in data:
        print(f"i see '->' in the data")
        data = data.split()[3]
        for x in data:
            if x.isalpha():
                data = data.replace(x, "")
        data = int(data)
        fibo = getFibonnaci(data)
        s.sendall(fibo.encode())
    else:
        break


