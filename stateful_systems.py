#!/usr/bin/python3
import socket
import sys

#SOCKET INFORMATION
target = "challenges.ctfd.io"
port = 30074
maxbuffer = 4096

# search for cities and states
def get_city_state(line):
    return line.strip().split(",")

#create a dictionary using cities and states
city_state_dict = dict()

# open the file
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        city_state = get_city_state(line)
    # add city and state to the dictionary that was created
        city = city_state[0].strip()
        state = city_state[1].strip()
        if city not in city_state_dict:
            city_state_dict[city] = state

#print(city_state_dict)

# CONNECT TO SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port))
# WHILE THE CONNECTION IS UP
while True:
    data = s.recv(maxbuffer).decode()
    print(f"{data}")

    # if 'is the capitol of which state' is in the data, look for the state that that CITY is the capitol of
    if "is the capitol of which state" in data:
        # for every city in the dictionary
        for city in city_state_dict.keys():
            # if the city key is in the data
            if city in data:
                # print the associated city key for that state value 
                city = city_state_dict[city]
                print(f"--> {city} <--\n")
                s.sendall(city.encode())
  #if 'what is the capitol of' is in the data, look for the capitol city of that state
    elif "What is the capitol of" in data:
        # for every state in the dictionary values
        for city, state in city_state_dict.items():
            if state in data:
                # print the associated state value for that city key
                print(f"--> {city} <--\n")
                s.sendall(city.encode())

    else:
        
        break





