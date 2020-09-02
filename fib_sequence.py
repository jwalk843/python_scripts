# user max
usermax = int(input("How many numbers do you want to see? "))

# start a counter, set it to 1
counter = 1
# start with a number left_hand as 0
left_hand = 0
# start with a number right_hand as 1
right_hand = 1
# while the counter is not over 100
while not counter > usermax:

    # print the number in left_hand
    # as coounter = left_hand
    print(f"#{counter} = {left_hand}")

    # calculate the desk as (sum of left_hand + right_hand)
    desk = left_hand + right_hand

    # rotate the numbers clockwise (left_hand goes to right_hand, right_hand goes to desk, etc)
    left_hand = right_hand
    right_hand = desk

    # increment the counter
    # counter = counter + 1
    counter += 1

