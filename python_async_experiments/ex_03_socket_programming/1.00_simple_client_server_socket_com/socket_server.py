#!/usr/bin/python3.6

import socket

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8086))
    server_socket.setblocking(True)
    server_socket.listen(1)
    (conn, addr)  = server_socket.accept()

    while True:
        data = conn.recv(8192)
        # print (data.decode())
    
if __name__ == "__main__":
    main()
