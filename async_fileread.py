#!/usr/bin/python3.6

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from itertools import islice


def long_time_task(fd, chunk_size):
	# emulating a long lasting blocking task
	time.sleep(2)
	return tuple(islice(fd, chunk_size))


async def async_read(executor, f_path, chunk_size, queue):
	with open(f_path, 'r') as fd:
		while True:
			#await asyncio.sleep(3)
			#data = tuple(islice(fd, chunk_size))
			#data = long_time_task(fd, chunk_size)
			data = await loop.run_in_executor(executor, long_time_task, fd, chunk_size)
			if not data:
				break
			if queue.full():
				print("Queue FULL")
			await queue.put(data)
			print("[READER] putted into queue: {}".format(data))


async def async_consume(queue):
	while True:
		data = await queue.get()
		print("[CONSUMER] consuming: {}".format(data))
		await asyncio.sleep(7)
		print("[CONSUMER] finished consuming {}".format(data))
		queue.task_done()


async def main(executor):
	queue = asyncio.Queue(3)
	consumer = asyncio.ensure_future(async_consume(queue))
	await async_read(executor, "data/test.file", 3, queue)
	await queue.join()
	consumer.cancel()


if __name__ == "__main__":
	executorPool = ThreadPoolExecutor(3)
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main(executorPool))
	loop.close()
