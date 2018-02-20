#!/usr/bin/python3.6

import timeHandler

f_pathu = "/media/andre/HDD/TkData/sorted/test_file.txt"
f_paths = "/media/andre/HDD/TkData/sorted/test.file"
f_pathl = "/media/andre/HDD/TkData/sorted/filtered_null_and_empty/" + \
          "motionl_MT_ngprs_T.out.20160915_sorted_4"


@timeHandler.timeit
def read_sequential():
    with open(f_pathl) as fd:
        for line in fd:
            pass


if __name__ == "__main__":
    read_sequential()
