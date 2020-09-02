#!/usr/bin/python3
import sys

def get_ip_from_file(line):
    
    return line.split()[0]
    

if __name__ == "__main__":
    
    # Constants for command-line operation
    NUM_ARGS = 2 # scriptname + logfile_name

    # Check our arguments and show
    # usage if we didn't get enough
    # (and then exit)
    if len(sys.argv) != NUM_ARGS:
        print("Running! But you forgot an argument or 2")
        print(f"Usage: {sys.argv[0]} LOG_FILE_NAME")
        sys.exit()
 
    # if we're good on args, then open the file and go
    # through every line
    ip_counts = dict() # str ip --> int number of counts
    with open(sys.argv[1], "r") as log_file:
        for line in log_file:
            # get the ip from the line
            ip_addr = get_ip_from_file(line)

            # store it in a dictionary and
            # track the count
            if ip_addr not in ip_counts:
                ip_counts[ip_addr] = 1
            else:
                ip_counts[ip_addr] += 1 # we saw the ip again so we're using an incrementer
    # from the dictionary, go through all keys
    # and add them to a nested list with: (count, ip)
    list_of_ips = list()
    for ip_addr in ip_counts.keys():
        list_of_ips.append((ip_counts[ip_addr], ip_addr))

    # sort the IP's by counts in 
    #descending order
    list_of_ips.sort(reverse=True)


    # print the top 4 IP's
    for count_ip_pair in list_of_ips[:4]:
        print(f"{count_ip_pair[1]}={count_ip_pair[0]}", end=",")