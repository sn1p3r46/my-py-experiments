#!/usr/bin/python3
import time
import timeHandler

from itertools import islice

f_pathl = "/media/andre/HDD/TkData/sorted/filtered_null_and_empty/" + \
                  "motionl_MT_ngprs_T.out.20160915_sorted_4"


def chunker(path, chunk_size=10):
    assert chunk_size > 0
    with open(path) as f:
        while True:
            res = tuple(islice(f,chunk_size))
            if not res: break
            else: yield res


@timeHandler.timeit
def read_chunker_gen(chunk_size):
    for i in chunker(f_pathl, chunk_size):
        lines = i


if __name__ == "__main__":

    read_chunker_gen(5000000)
    read_chunker_gen(2000000)
    read_chunker_gen(1000000)
    read_chunker_gen(500000)
    read_chunker_gen(250000)
    read_chunker_gen(125000)
    read_chunker_gen(75000)
    read_chunker_gen(20000)
    read_chunker_gen(10000)
    read_chunker_gen(50000)
    read_chunker_gen(2500)
    read_chunker_gen(1000)
    read_chunker_gen(500)
    read_chunker_gen(100)
    read_chunker_gen(50)
