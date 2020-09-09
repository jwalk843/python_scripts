#!/usr/bin/python3
import sys
import os
import hashlib
import shutil

"""
Runcode CTF program submission
"""


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
        try:
            os.mkdir("temp")

        except FileExistsError as e:
            print(f"{e}: The directory already exists")
        finally:
            my_input = sys.argv[1]
            main_directory = os.path.abspath(my_input)
            print(f"Target Directory: {main_directory}")
            temp_directory = os.path.abspath("temp")
            print(f"Temp Directory is: {temp_directory}")

            # look for the directories
            # create a list to store the names
            dirs_list = []
            # print(f"Directories found...")
            # for each subdirectory in the current working directory
            for subdir in os.listdir(sys.argv[1]):
                rel_directory = os.path.join(main_directory, subdir)
                # Change to the subdirectory
                os.chdir(rel_directory)
                # print(os.listdir('.'))
                for file in os.listdir("."):
                    if file.endswith(".txt"):
                        # print(f"\tCopying {file} to the temporary directory")
                        shutil.copy(file, temp_directory)
                # print(f"Listing contents of temp")
            temp_directory_sorted = sorted(os.listdir(temp_directory))
            print(f"Preparing to hash the files in {temp_directory}")
            os.chdir(temp_directory)
            for file in temp_directory_sorted:
                print(hashFiles(file))
