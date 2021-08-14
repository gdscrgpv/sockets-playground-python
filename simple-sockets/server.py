#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # Binds the socket to the port
    s.bind((HOST, PORT))

    # Listen for incoming connections
    s.listen()
    print("Binded to IP {} on port {}".format(HOST,PORT))

    # Accept connections
    conn, addr = s.accept()
    
    with conn:
        print('Connected by', addr)
        while True:

            # Receives data from the client
            # 1024 means max data, it doesn’t mean that recv() will return 1024 bytes.
            data = conn.recv(1024)
            if not data:
                break

            # Sends the data back to the client
            conn.sendall(b"server says "+data)