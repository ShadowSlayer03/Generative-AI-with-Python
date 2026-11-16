import threading
import time

import requests

# Threads are not applicable everywhere simply because of GIL that has a mutex that makes sure only 1 thread executes at a time

# Use cases where threads shine:
# I/O bound operations - read/write
# DB query
# Web Requests

# Reason is because while one thread waits for something, it can release the GIL, allowing another thread to execute

def download(url):
    print(f"Starting download from {url}...")
    response = requests.get(url)
    print("Response code:", response.status_code)
    print(f"Download finished from url {url}, size {len(response.content)} bytes")

urls = [
    'https://httpbin.org/image/jpeg',
    'https://httpbin.org/image/png',
    'https://httpbin.org/image/svg',
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end-start:.2f} seconds")
