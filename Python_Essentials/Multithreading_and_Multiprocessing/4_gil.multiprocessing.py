import time
from multiprocessing import Process


# Important thing to note about GIL is that it is tied to a process
# A process can have multiple threads so all threads make use of the GIL to prevent any overwriting
# In multiprocessing, like we see here each process has its own GIL
def crunch_number():
    print("Starting the count process...")
    count = 0
    for _ in range(100_000_000):
        count+=1
    print("Ended the count process")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi processing is {end-start} seconds")
