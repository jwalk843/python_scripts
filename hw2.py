#!/usr/bin/python3

# GET A NUMBER FROM THE USER
user_num = input()
# WHILE IT'S A VALID NUMBER
while user_num.isdigit():
    # CONVERT IT TO A NUMBER
    user_num = int(user_num)
    # ASSUME THE NUMBER IS PRIME
    is_prime = True

    # DETERMINE IF THE NUMBER IS PRIME
    # go through all numbers from 2 to num ** (0.5) + 1 see
    # if it divides evenly, not prime
    min_try = 2
    max_try = (user_num ** 0.5) + 1
    curr_try = min_try
    while not curr_try > max_try:
        if user_num % curr_try == 0:
            is_prime = False
            break
        curr_try += 1
    # IF NUMBER IS PRIME, PRINT IT
    if is_prime or user_num == 2:
        print("Prime!")
    # OTHERWISE, PRINT NOT PRIME.
    else:
        print("Not prime!")
    # GET ANOTHER NUMBER FROM USER
    user_num = input()
