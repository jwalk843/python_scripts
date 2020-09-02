import sys
import os
import hashlib

def get_checksum(input_fname):
    """
    given the input_fname, open and 
    read the file, the return the md5 hash (as a str) of the file
    contents.

    args:
        inputfname: (str) input filename

    returns a string (the md5 hash)

    """
    with open(input_fname, "rb") as infile:
        file_contents = infile.read()

    checksum = hashlib.md5(file_contents).hexdigest()
    return checksum

# This script was run directly
if __name__ == "__main__":

    # Constants for command-line operation
    NUM_ARGS = 2

    # Check our arguments and show
    # usage if we didn't get enough
    # (and then exit)
    if len(sys.argv) != NUM_ARGS:
        print(f"Usage: {sys.argv[0]} TEXT")
        sys.exit()
    
    hashes = {} # fhash -> [fname1, fname2, fname3]
    # if we got enough, then loop through all
    # files in our target direcory
    # for every file, store the md5 hash
    for fname in os.listdir(sys.argv[1]):
        # get the relative path
#        rel_fname = f"{sys.argv[1]}{os.sep}{fname}" this is one way
        rel_fname = os.path.join(sys.argv[1], fname)

        # calculate the hash of the file
        checksum = get_checksum(rel_fname)
        
        # store it or add it to the list if there is alread
        # a file with this hash
        if checksum not in hashes:
            hashes[checksum] = [rel_fname]
        else:
            hashes[checksum].append(rel_fname)

    # after calculating the hashes for every file
    # loop through all the hashes and print out every
    # key that has more than one file with the same hash
    for hash_key in hashes.keys():
        
        # is there more than one file with this hash?
        if len(hashes[checksum]) > 1:
            print(f"Files with checksum {checksum}")
            for fname in hashes[checksum]:
                print(f"\t{fname}")
