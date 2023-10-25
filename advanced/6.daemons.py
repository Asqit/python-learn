# Daemon Thread
# is a thread that runs in the background and is not important for the program to run
# Deamon threads can be used for: Background-tasks, waiting for input, running-processes, garbage-collecting
# The difference between daemon thread and non-deamon thread is that when main thread ends, it will automatically
# kill any daemon thread, while with regular threads the main thread will wait for them to finish.

import threading
import time


def timer() -> None:
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Waiting for {count} seconds")


daemon = threading.Thread(target=timer, daemon=True)
daemon.start()


# Do you know why it works this way?
# The main thread have nothing else to do, but to wait for the user_input to catch value from input.
# although the timer is defined, it is never runned by the main thread.
# So, logically, when you enter the input, there is nothing else to do for the main thread and so it will
# end and with that the daemon will too. If daemon variable was non-daemoning thread, the main thread would have to
# wait for it to finish.
user_input = input("Do you wish to quit?: ")
