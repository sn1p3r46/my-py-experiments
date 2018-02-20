#!/usr/bin/python3.6

import socket

f_path = '/run/media/andre/HDD/TkData/sorted/'
f_name = 'motionl_MT_ngprs_T.out.20161001_sorted_4'


def my_endless_iterator():
    i = 0
    while True:
        yield i
        i += 1


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8086))

    with open(f_path + f_name, 'rb') as f_handler:
        payload = " "
        i = 0

        while payload:
            i += 1
            payload = f_handler.read(8192)
            s.sendall(payload)

            if i % 100_000 == 0:
                print(i)

        print("END")


if __name__ == "__main__":
    main()
