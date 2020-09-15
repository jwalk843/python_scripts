#!/usr/bin/python3
import socket
import sys

class ConnectClass():
    """
    My custom client server
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port

        # Establish the connection to the target:port
        print(f"Connecting to {self.host}:{self.port}...")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.host, self.port))
        except OSError as e:
            print(e)

    def recv_data(self, maxbuffer=4096):
        """
        Receive the data from the server
        """
        try:
            buff = self.s.recv(maxbuffer)
        except OSError as e:
            print(e)
        return buff.decode()
        
    def send_data(self, str_data):
        """
        Send the data to the server
        """
        try:
            self.s.sendall(str_data.encode())
        except OSError as e:
            print(e)
