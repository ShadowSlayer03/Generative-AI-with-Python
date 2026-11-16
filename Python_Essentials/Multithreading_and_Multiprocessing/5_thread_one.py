import threading
import time

# Multithreading:
# -  Concurrency
# - multiple threads created that belong to a single process and share memory
# - useful for tasks that take time, switching context is not an issue
#
# Async IO
# - Concurrency
# - multiple tasks created that belong to the same thread
# - only useful when there are asynchronous operations like fetching an API request where for multiple operations, managing multiple threads might not always be useful
#
# Multiproocessing
# - Parallelism
# - multiple processes created that have its own memory and CPU
# - useful for CPU intensive tasks

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk boiled")

def toast_bun():
    print("Toasting bun...")
    time.sleep(3)
    print("Bun toasted")

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Process ended in {end-start:.2f} seconds")
