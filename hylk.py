#!/usr/bin/python3
import sys
import os
import hashlib
import shutil


def hashFiles(fname):
    # open the files and hash the contents
    with open(fname, "rb") as f:
        content = f.read()
    checksum = hashlib.sha1(content).hexdigest()
    return checksum


if __name__ == "__main__":

    NUM_ARGS = 2
    if len(sys.argv) != NUM_ARGS:
        print(f"USAGE: {sys.argv[0]} + Target_directory")
        sys.exit()

    # create a directory to hold the files that will be hashed
    if not os.path.realpath(os.curdir).endswith("heard_you_like_hashes"):
        os.chdir(os.path.realpath("heard_you_like_hashes"))
    else:
        my_input = sys.argv[1]
        main_directory = os.path.abspath(my_input)
        # print(f"Target Directory: {main_directory}")
        temp_directory = os.path.abspath("temp")
        # print(f"Temp Directory is: {temp_directory}")

        # create a list for the text files
        textfiles = []
        # walk the directory to see what's all in it
        for root, dirs, files in os.walk(main_directory):
            textfiles.append(files)
        
        for each in textfiles:
            if '.txt' in each:
                try:
                    shutil.copy(each, temp_directory)
                except FileNotFoundError as e:
                    print(e)
          
            # print(f"Listing contents of temp")
        temp_directory_sorted = sorted(os.listdir(temp_directory))
        # print(f"Preparing to hash the files in {temp_directory}")
        # print(f"=========================================")
        os.chdir(temp_directory)
        for file in temp_directory_sorted:
            # print(f"{file}--> {hashFiles(file)}")
            hashcheck = hashFiles(file)
            # add each hash to the other to create one bigass hash
            hashcheck = hashcheck
            hashcheck += hashcheck
            # print(hashcheck)
        # hash the bigass hash :)
        hashcheck = hashcheck.encode()
        h = hashlib.sha1(hashcheck).hexdigest()
        # print(f"the hash of the bigass hash is.....")
        print(h)
