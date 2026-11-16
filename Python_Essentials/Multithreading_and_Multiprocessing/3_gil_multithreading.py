# GIL is Global Interpreter Lock
# Race condition is when more than one thread tries to access the same memory and modify it
# GIL is a mutex (mutual exclusion) that allows only one thread to execute Python bytecode at a time in a conventional interpreter
# In this case each thread is modifying its own variable so no chance of race condition

import threading
import time


def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count+=1
        print("count:", count)
    print(f"{threading.current_thread().name} finished brewing...")

barista1 = threading.Thread(target=brew_chai, name="Barista-1")
barista2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()

barista1.start()
barista2.start()

barista1.join()
barista2.join()

end = time.time()

print(f"Total time taken: {end - start} seconds")
