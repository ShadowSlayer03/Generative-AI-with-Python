import time
from multiprocessing import Process


# Example of multiprocessing
# Parallelism where multiple cores are used and each process is working independently of the other
def brew_chai(name):
    print(f"Start of brewing chai: {name}")
    time.sleep(3)
    print(f"End of brewing chai: {name}")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", )) for i in range(3)
    ]

    for p in chai_makers:
        p.start()

    # Waiting for each process to complete
    for p in chai_makers:
        p.join()

    print("All chai served!")
