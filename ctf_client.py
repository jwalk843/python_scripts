#!/usr/bin/python3
import socket
# gets response from server and prints it out

SOCKET = None
MAXBUF = 4096

def get():
    data = SOCKET.recv(MAXBUF)
    return data.decode()

def send(data):
    SOCKET.sendall(data.encode())

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SOCKET.connect(("challenges.ctfd.io", 30070))

data_in = get()
print(data_in)
send("100")
data_in = get()
print(data_in)

