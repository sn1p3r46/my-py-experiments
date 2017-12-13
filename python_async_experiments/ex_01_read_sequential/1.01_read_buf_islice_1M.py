#!/usr/bin/python3.6

import datetime 
import timeHandler

from os.path import basename
from itertools import islice



f_pathu = "/media/andre/HDD/TkData/sorted/test_file.txt"
f_paths = "/media/andre/HDD/TkData/sorted/test.file"  
f_pathl = "/media/andre/HDD/TkData/sorted/filtered_null_and_empty/" + \
          "motionl_MT_ngprs_T.out.20160915_sorted_4"

N = 1000000
NS = 100

@timeHandler.timeit
def read_buf_islice(N=N):
    with open(f_pathl) as fd:
        while True:
            lines = tuple(islice(fd, N))
            if not lines:
                break

if __name__ == "__main__":
    read_buf_islice()
    read_buf_islice(5000000)
    read_buf_islice(2000000)
    read_buf_islice(1000000)
    read_buf_islice(500000)
    read_buf_islice(250000)
    read_buf_islice(125000)
    read_buf_islice(75000)
    read_buf_islice(20000)
    read_buf_islice(10000)
    read_buf_islice(5000)
    read_buf_islice(2500)
    read_buf_islice(1000)
    read_buf_islice(500)
    read_buf_islice(100)
    read_buf_islice(50)
