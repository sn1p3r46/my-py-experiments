#!/usr/bin/python3.6

import datetime
import timeHandler

from os.path import basename
from itertools import islice

f_pathu = "/media/andre/HDD/TkData/sorted/test_file.txt"
f_paths = "/media/andre/HDD/TkData/sorted/test.file"
f_pathl = "/media/andre/HDD/TkData/sorted/filtered_null_and_empty/" + \
          "motionl_MT_ngprs_T.out.20160915_sorted_4"


@timeHandler.timeit
def read_buf_islice(N):
    with open(f_pathl) as fd:
        while True:
            lines = tuple(islice(fd, N))
            if not lines:
                break


if __name__ == "__main__":

    vals = [5000000,2000000,1000000,500000,
            250000,125000,75000,20000,10000,
            5000,2500,1000,500,100,50]

    for val in vals:
        read_buf_islice(val)
