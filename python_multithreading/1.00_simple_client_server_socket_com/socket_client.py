#!/usr/bin/python3.6

import queue
import threading
import socket
from timeHandler import timeit
import os

dir_path = '/run/media/andre/HDD/TkData/sorted/filtered_null_and_empty'
# f_name = 'motionl_MT_ngprs_T.out.20161001_sorted_4'


@timeit
def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8086))

    file_list = os.listdir(dir_path)
    file_list.sort()

    q = queue.Queue(maxsize=100)

    def send():
        while True:
            payload = q.get()

            if payload is None:
                print("[thread]> Payload is None: exiting...")
                q.task_done()
                return

            s.sendall(payload)
            q.task_done()

    thread = threading.Thread(target=send)
    thread.start()

    i = 0

    for f_name in file_list[-1:]:
        with open(os.path.join(dir_path, f_name), 'rb') as f_handler:
            print(f"START {f_name}")
            payload = True
            i += 1
            while payload:

                payload = f_handler.read(8192)

                if not payload:
                    break

                q.put(payload)

            print(f"END {f_name}")

    print("Joining!")
    q.join()
    q.put(None)
    thread.join()

    print(f"Number of file Processed: {i}")


if __name__ == "__main__":
    main()
