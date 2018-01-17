#!/usr/bin/python3.6

import socket
from itertools import islice

f_path = '/home/andrea/Documents/ELTE/pythonlogprocessing/data/computed/logs_sample/'
f_name = 'motionl_MT_ngprs_T.out.20161001_sorted_4'
 

def my_endless_iterator():
    i = 0

    while True:

        yield i
        i+=1 


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8086))
    myter = my_endless_iterator()
    a = open(f_path + f_name, 'rb')
    payload = " "
    i = 0

    while payload:

        i+=1 
        # msg = (','.join([str(val) for val in islice(myter,99)])+"\n").encode()
        payload = a.read(8192)
        s.sendall(payload) 
        if i % 100_000 == 0:
            print (i)

    a.close()
    print ("ciaone")

if __name__ == "__main__":
    main()

