#!/usr/bin/python3.6

import datetime


def timeit(func):
    def timeme(*args, **kwargs):
        t0 = datetime.datetime.now()
        res = func(*args, **kwargs)
        t1 = datetime.datetime.now()
        print("Execution of file: {}({},{})\nTIME ELAPSED: {}".format(
                func.__name__, args, kwargs, t1-t0))
        return res

    return timeme
