# As I said in threading.py
# Processes are used to handle expensive functions
from multiprocessing import Process, cpu_count
import time


# Example of very expensive function
def counter(num=1_000_000_000):
    count = 0

    while count < num:
        count += 1


def main():
    start_delta = time.perf_counter()

    # By distributing the load to multiple processes
    # we improve the performance
    # with single process counting to 1_000_000_000
    # took 55s for single process
    # and 29s for two processes
    # and 22s for four processes
    # but depending on your processor the result might even be worse
    # because you might spawn more processes than you have cores
    # and that would cause that one core would have to work on more process
    # for that see spawn_workers function
    a = Process(target=counter, args=(250_000_000,))
    b = Process(target=counter, args=(250_000_000,))
    c = Process(target=counter, args=(250_000_000,))
    d = Process(target=counter, args=(250_000_000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    end_delta = time.perf_counter()

    print(f"Finished in {end_delta - start_delta} sec")


def spawn_workers():
    # It is better to distribute the work to multi-processes
    # but we should not abuse the cpu cores by loading more than one process for each
    workload = 1_000_000_000
    processes: list = []
    cores = cpu_count()

    for _ in range(cores):
        processes.append(Process(target=counter, args=((workload / cores),)))

    start_delta = time.perf_counter()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_delta = time.perf_counter()

    print(f"Finished in {end_delta - start_delta} sec")


if __name__ == "__main__":
    spawn_workers()
