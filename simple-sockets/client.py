#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to socket
    s.connect((HOST, PORT))

    # Send data from client to server
    s.sendall(b'Hello, world')

    # Receive data from server
    data = s.recv(1024)

print('Received', repr(data))