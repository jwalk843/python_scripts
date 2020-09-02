#!/usr/bin/python3

def getFib(str2): 
    usermax = str2
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
            if counter == str2:
                answer = f"{v}".strip()
                return answer

getFib(48)
