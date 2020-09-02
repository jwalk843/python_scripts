import socket
import sys

# make a connection to 'challenges.ctfd.io:30069'
# print the response
target = "challenges.ctfd.io"
port = 30069

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target,port))
print(s.recv(1024).decode())
s.sendall(b'Navy')
print(s.recv(1024).decode())


