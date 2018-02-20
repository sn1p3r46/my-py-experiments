#!/usr/bin/python3.6

import socket


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8086))
    server_socket.setblocking(True)
    server_socket.listen(1)
    (conn, addr) = server_socket.accept()

    last_suffix = ""
    i = 0

    while True:

        bin_data = conn.recv(8192)
        if not bin_data:
            break

        # Convert from binary to UTF-8 string
        raw_data = bin_data.decode().split('\n')
        # Injects the previous suffix
        raw_data[0] = last_suffix + raw_data[0]
        # Stores the last_suffix
        last_suffix = raw_data[-1]
        clean_data = raw_data[:-1]

        i += 1

        if clean_data[0] == "":
            print("\n\nERROR 0 \n\n")

        if clean_data[-1] == "":
            print("\n\nERROR -1 \n\n")


if __name__ == "__main__":
    main()
