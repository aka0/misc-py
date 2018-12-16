""" Testing python3 multiprocessing with a job queue """

import multiprocessing as mp
from random import randint
import time


def rand_sleep(seconds, i):
    print(f'Sleeping {seconds} by {i}')
    time.sleep(seconds)


def process_job(q, i):
    while not q.empty():
        s = q.get()
        rand_sleep(s, i)
    print(f'DONE - {i}')


def main():
    num_cpu = mp.cpu_count()
    print(f'Testing multiprocessing with queue, using {num_cpu}')

    # Fill job queue with 100 jobs
    jobs = mp.Queue()
    for j in range(10):
        jobs.put(randint(0, 10))

    processes = []
    for i in range(num_cpu):
        p = mp.Process(
            target=process_job, args=(
                jobs,
                i,
            ))
        p.start()
        processes.append(p)

    for proc in processes:
        proc.join()


if __name__ == "__main__":
    main()
