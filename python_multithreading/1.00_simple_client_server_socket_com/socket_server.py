#!/usr/bin/python3.6

import socket
import threading
import queue


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8086))
    server_socket.setblocking(True)
    server_socket.listen(1)
    (conn, addr) = server_socket.accept()

    i = 0
    q = queue.Queue(100)

    def consume():

        last_suffix = ""
        while True:

            bin_data = q.get()

            if bin_data is None:
                q.task_done()
                return

            raw_data = bin_data.decode().split('\n')
            # Injects the previous suffix
            raw_data[0] = last_suffix + raw_data[0]
            # Stores the last_suffix
            last_suffix = raw_data[-1]
            clean_data = raw_data[:-1]

            if clean_data[0] == "":
                print("\n\nERROR 0 \n\n")

            if clean_data[-1] == "":
                print("\n\nERROR -1 \n\n")

            q.task_done()

    thread = threading.Thread(target=consume)
    thread.start()

    while True:

        bin_data = conn.recv(8192)
        if not bin_data:
            q.put(None)
            break
        q.put(bin_data)

        i += 1

    q.join()
    q.put(None)
    thread.join()


if __name__ == "__main__":
    main()
