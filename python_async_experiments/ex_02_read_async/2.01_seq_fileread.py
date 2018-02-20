#!/usr/bin/python3.6

import time
from itertools import islice


def read(f_path, chunk_size):
    # open the file
    with open(f_path, 'r') as fd:
        while True:
            data = tuple(islice(fd, chunk_size))
            time.sleep(3)

            if not data:
                break

            print("[GENERATOR] Just yielded: {}".format(data))
            yield data


def consume():
    for data in read("data/test.file", 3):
        print("[CONSUMER] consuming: {}".format(data))
        # Emulates a long async task
        time.sleep(7)
        print("[CONSUMER] finished consuming {}".format(data))


if __name__ == "__main__":
    consume()
