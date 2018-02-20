#!/usr/bin/python3.6

import socket


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8086))
    server_socket.setblocking(True)
    server_socket.listen(1)
    (conn, addr) = server_socket.accept()

    last_postfix = ""
    i = 0

    while True:
        # Receives 8192 Bytes
        bin_data = conn.recv(8192)
        if not bin_data:
            break
        # Convert from binary to UTF-8 string
        raw_data = bin_data.decode()
        # Get the index of last '\n' suffix
        last_postfix_index = raw_data.rfind("\n")
        # Removes the last suffix and injects the previous suffix
        clean_data = last_postfix + raw_data[:last_postfix_index]
        # Store the last postfix removing the '\n' char
        last_postfix = raw_data[last_postfix_index + 1:]

        i += 1

        data = clean_data.split("\n")

        if data[0] == "":
            print("\n\nERROR\n\n")


if __name__ == "__main__":
    main()
