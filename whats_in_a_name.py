#!/usr/bin/python3
import socket
import sys
import requests

#SOCKET INFORMATION
target = "challenges.ctfd.io"
port = 30073
maxbuffer = 4096

def find_the_Admiral(name):
    with open("admiralslist.txt", "r") as inputfile:
        if name in inputfile.read():
            return True
        else:
            return False
    
# Who is the four-star Admiral in this group: Lynde D. McCormick, Raymond V. Fleming, Jared E. Mack, Courtney A. Barker, Kayla T. Ray? 

# CONNECT TO SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port))
# WHILE THE CONNECTION IS UP

admiral_names = []

while True:
    data = s.recv(maxbuffer).decode()
    print(data)

    if "Who is the four-star Admiral in this group" in data:

        stripped_data = data.replace("?", "").split(":")[1].split(",") 
        print(stripped_data)        
        
        # get a list of all four-star admirals and put them into a list
        for name in stripped_data:
            name = name.strip()
            admiral_names.append(name)
        #print(f"List: {admiral_names}")
        # for each name in the admiral name list, see if they are mentioned on the wiki site
        print(f"List: {admiral_names}")

        for each_name in admiral_names:
            # for each name, check if their name is in the document
        
            find_the_admiral = find_the_Admiral(each_name)

            if find_the_admiral == True:

                print(f"\tYES, {each_name} is an Admiral\n")

                s.sendall(each_name.encode())
                
    
    elif "Who is the four-star Admiral in this group" not in data:
        print(f"Gonna parse some names...")
        # strip it down to just names of the potential admirals
        data = data.split(",")
        # put the names into another list
        new_admirals_list = []
        for elements in data:
            elements = elements.replace("?", "").strip()
            new_admirals_list.append(elements)
        print(f"List: {new_admirals_list}")
        # for each name in the new list, run the 'find_the_admiral' function against it
        for each_name in new_admirals_list:
            find_the_admiral = find_the_Admiral(each_name)
            if find_the_admiral == True:
                print(f"\tYES, {each_name} is an Admiral\n")
                s.sendall(each_name.encode())
                break
        
                
        # if the function is true, send the name to the server

        # if the function is false, break the loop
    else:
        break

