import threading
import time


def prepare_chai(chai_type, quantity):
    print(f"Preparing chai {chai_type} for {quantity} people...")
    time.sleep(3)
    print(f"{chai_type} chai prepared!")

t1 = threading.Thread(target=prepare_chai, args=("Ginger",2))
t2 = threading.Thread(target=prepare_chai, args=("Masala",4))

t1.start()
t2.start()

t1.join()
t2.join()
