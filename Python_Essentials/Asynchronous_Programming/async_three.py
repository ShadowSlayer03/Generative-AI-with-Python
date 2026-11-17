import asyncio
import time

import aiohttp

async def fetch_url(session,url):
    start = time.time()
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")
        html = await response.text()
        print("Body:", html[:15], "...")
    end = time.time()
    print(f"Fetch over in {end-start} seconds!")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)
    end = time.time()
    print(f"\nTotal fetches over in {end-start} seconds!")

asyncio.run(main())
