# Threading
# Concurrency is topic in programming, where we try to program a way to do multiple things in once
# Python has few way to manage concurrency:
# -------------------------------------------------------------------------------------------------
# 1. Threads (import threading)
# You can use multiple cores of your CPU at once and each core will do it's part of the job.
# Threads are useful for dealing with I/O bound task (Where program is waiting for input or output)
# -------------------------------------------------------------------------------------------------
# 2. Processes (import multiprocessing)
# Python also have processes. These are separate instance of the python interpreter
# These processes work independetly of each other and are used for heavy CPU tasks (calculations...)
# -------------------------------------------------------------------------------------------------
# 3. Async (import asyncio)
# Python can also mimic asynchronous programming. This may reduce the load to threads  or processes
# It works similiarly to JavaScript, where you have async/await keywords.
# You mark "async" a function that waits for something to finish.
# To mark something that requires time to finish you use "await" keyword
import threading
import time


# Example_1 (Mark Wattney cooking potatoes :D)
def prepare_potatoes():
    time.sleep(2)
    print("Potatoes are naked and sliced to cubicles")


def boil_potatoes():
    time.sleep(5)
    print("Potatoes are boiling in 100C water")


def eat():
    time.sleep(4)
    print("Enjoy your potatoes, Wattney!")


# This is done sequentialy
# prepare_potatoes()
# boil_potatoes()
# eat()

# But we can multi-task with threads
x = threading.Thread(target=prepare_potatoes, args=())
x.start()

y = threading.Thread(target=boil_potatoes)
y.start()

z = threading.Thread(target=eat)
z.start()

# We can also wait for another thread to finish it's job
y.join()

# By using threads we reduce the time of the script

# Amount of running threads
print(threading.active_count())

# List of threads
print(threading.enumerate())

print("PERF_OF_THE_MAIN_THREAD: " + str(time.perf_counter()))
