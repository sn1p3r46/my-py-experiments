#!/usr/bin/python3
import timeHandler

from itertools import islice

f_pathl = "/media/andre/HDD/TkData/sorted/filtered_null_and_empty/" + \
                  "motionl_MT_ngprs_T.out.20160915_sorted_4"


def chunker(path, chunk_size=10):
    assert chunk_size > 0
    with open(path) as f:
        while True:
            res = tuple(islice(f, chunk_size))
            if not res:
                break
            else:
                yield res


@timeHandler.timeit
def read_chunker_gen(chunk_size):
    for i in chunker(f_pathl, chunk_size):
        # USELESS
        lines = i


if __name__ == "__main__":

    vals = [5000000, 2000000, 1000000, 500000,
            250000, 125000, 75000, 20000, 10000,
            50000, 2500, 1000, 500, 100, 50]

    for val in vals:
        read_chunker_gen(val)
