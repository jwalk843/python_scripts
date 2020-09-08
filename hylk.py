#!/usr/bin/python3
import sys
import os
import hashlib
import shutil

"""
Look through all of the directories and subdirectories and collect all t
he files. Once they are all collected, sort by just the filename (0-9A-Za-z) 
and not the entire path, iterate over each file in a sorted fashion (0-9A-Za-z), and 
get the sha1 hash of each file. Combine all the hashes to create a mega hash and 
hash that hash. The output is a single sha1 hash. If any of the content in 
the directory changes, the final hash will also change. This gives you the 
means to quickly check the overall forensic integrity 
of a directory (or even an entire file system). 
The input will be a path to a file system to hash.
"""
def parseDirectories(dname):
    print(f"Parsing {dname} directory now...")
# look for the directories
    # create a list to store the names
    dirs_list = []
    print(f"Directories found...")
    for dname in os.listdir(dname):
        print(dname)

def hashFiles(dname):
    # hash the files in the directory 
    pass

if __name__ == "__main__":

    NUM_ARGS = 2
    if len(sys.argv) != NUM_ARGS:
        print(f"USAGE: {sys.argv[0]} + Target_directory")
        sys.exit()
    
    # create a directory to hold the files that will be hashed
    try:
        os.mkdir('temp')
    except FileExistsError as e:
        print(f"{e}: The directory already exists")
    finally:
        # get a list of the folders in the directory
        files_list = []
        parseDirectories(sys.argv[1])



