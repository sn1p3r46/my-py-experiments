#!/usr/bin/python3.6

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from itertools import islice

# +++++++++++++++++ WARNING THIS CODE CONTAINS ERRORS ON PURPOSE +++++++++++++++
# the behaviour of this code is intended to be error prone just for illustration


# This function does not contain any pythonic async mechanism and it is slow
def long_time_task(fd, chunk_size):
    # emulating a long lasting BLOCKING task
    time.sleep(4)
    # returns a chunk of a file
    return tuple(islice(fd, chunk_size))

# Emulates a reader task
async def async_read(executor, f_path, chunk_size, queue):
	# open the file
    with open(f_path, 'r') as fd:
        while True:
            # Uncomment for Asyncronous behaviour
            # RIGHT IMPL:
            # data = await loop.run_in_executor(executor, long_time_task, fd, chunk_size)
            data = long_time_task(fd, chunk_size)
            # EOF? Exit the loop then!
            if not data:
                break
            # Just a check for adjusting the length of the queue
            if queue.full():
                print("Queue FULL")
            # does not block the event loop if the queue is full
            await queue.put(data)
            print("[READER] putted into queue: {}".format(data))


# Emulates a consumer task
async def async_consume(queue):
	while True:
		# Does not block the event loop waiting for the queue being filled
		data = await queue.get()
		print("[CONSUMER] consuming: {}".format(data))
		# ERROR, it is a non-async long task
		time.sleep(7)
		print("[CONSUMER] finished consuming {}".format(data))
		queue.task_done()


async def main(executor):
	# Queue initialization with max 3 full slots
	# https://docs.python.org/3.5/library/asyncio-queue.html#queue
	queue = asyncio.Queue(maxsize=1)
	# We launch the consumer in the future, it does not block the code
	consumer = asyncio.ensure_future(async_consume(queue))
	print("Type of 'consumer = asyncio.ensure_future(async_consume(queue))': {}".format(type(consumer)))
	# Launches the data producer and performs a non blocking wait
	await async_read(executor, "data/test.file", 3, queue)
	# Wait until the queue is empty non blocking wait
	await queue.join()
	# All the chunks are now processed, we can cancel the consumer task safely
	consumer.cancel()


if __name__ == "__main__":
	# We prepare a pool of threads one is enough but we set the max up to 3
	executorPool = ThreadPoolExecutor(3)
	# get the default event loop
	loop = asyncio.get_event_loop()
	# We run the function until it is complete.
	loop.run_until_complete(main(executorPool))
	# We close the loop, from now on it is not usable but we need to create a new one.
	loop.close()
