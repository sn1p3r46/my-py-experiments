#!/usr/bin/python3.6

import collections
import time

dim = 5_000_000


def timeit(method):

    def timed(*args, **kw):

        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' %
                  (method.__name__, (te - ts) * 1000))

        return result

    return timed


@timeit
def arr_pop(arr):
    while arr:
        arr.pop()


@timeit
def que_pop(queue):
    while queue:
        queue.pop()


@timeit
def arr_pop0(arr):
    while arr:
        arr.pop(0)


@timeit
def que_popleft(queue):
    while queue:
        queue.popleft()


@timeit
def arr_pop_n_push(arr):
    for _ in range(len(arr)):
        x = arr.pop(0)
        arr.append(x)


@timeit
def que_pop_n_push(queue):
    for _ in range(len(queue)):
        x = queue.pop()
        queue.append(x)


@timeit
def que_rotate(queue):
    for _ in range(len(queue)):
        queue.rotate(1)


@timeit
def arr_for(arr):
    for i in arr:
        x = i


@timeit
def que_for(queue):
    for i in queue:
        x = i


@timeit
def arr_index(arr):
    for i in range(len(arr)):
        x = arr[i]


@timeit
def que_index(queue):
    for i in range(len(queue)):
        x = queue[i]


@timeit
def arr_insertion(arr):
    for i in range(len(arr)):
        arr.insert(i, i)


@timeit
def que_insertion(queue):
    for i in range(len(queue)):
        queue.insert(i, i)


@timeit
def arr_sum(arr):
    sum(arr)


@timeit
def deq_sum(queue):
    sum(queue)


if __name__ == "__main__":

    my_arr = list(range(dim))
    my_deq = collections.deque(range(dim))

    arr_pop(my_arr)
    que_pop(my_deq)

    my_arr = list(range(dim))
    my_deq = collections.deque(range(dim))

    arr_pop0(my_arr)
    que_popleft(my_deq)

    my_arr = list(range(dim))
    my_deq = collections.deque(range(dim))

    arr_pop_n_push(my_arr)
    que_pop_n_push(my_deq)
    que_rotate(my_deq)

    my_arr = list(range(dim))
    my_deq = collections.deque(range(dim))

    arr_for(my_arr)
    que_for(my_deq)

    my_arr = list(range(dim))
    my_deq = collections.deque(range(dim))

    arr_sum(my_arr)
    deq_sum(my_deq)

    my_arr = list(range(dim))
    my_deq = collections.deque(range(dim))

    arr_index(my_arr)
    que_index(my_deq)

    my_arr = list(range(dim))
    my_deq = collections.deque(range(dim))

    arr_insertion(my_arr)
    que_insertion(my_deq)
