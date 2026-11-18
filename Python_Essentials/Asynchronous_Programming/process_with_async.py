import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def encrypt(text):
    print("Starting encryption...")
    time.sleep(4)
    print("Encrypted text successfully")
    return text[::-1]

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "credit_card_1234")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
