#!/usr/bin/python3
ip_agents = dict() # ip_addr -> [agent1, agent2, agent3]

# Read through every line in the log file
with open("example.log", "r") as infile:
    for line in infile:

        # Grab the first six fields and extract the IP
        # and possible User-Agent string
        ip_container, _, _, _, _, poss_agent = line.split('"')[:6]
        ip = ip_container.split()[0]

        # Check if we've seen this ip before
        if ip not in ip_agents:
            # Add it
            ip_agents[ip] = [poss_agent]
        else:
            # We've seen the IP -- have we seen
            # the IP send this agent?
            if poss_agent not in ip_agents[ip]:

                # If not, add it to the list
                ip_agents[ip].append(poss_agent)

agents_ip = [(ip, len(ip_agents[ip])) for ip in ip_agents.keys()]

'''
agents_ip = []
for ip in ip_agents.keys():
    pair = (ip, len(ip_agents[ip]))
    agents_ip.append(pair)
'''

agents_ip.sort(reverse=True, key=lambda x:x[1])
for pair in agents_ip[:2]:
    print(f"\n\nIP address {pair[0]} sent user agents:")
    for agent in ip_agents[pair[0]]:
        print(f"\t{agent}")
