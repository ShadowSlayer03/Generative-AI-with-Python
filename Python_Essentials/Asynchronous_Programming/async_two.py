import asyncio


async def brew_chai(name):
    print(f"brewing chai {name}...")
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f"{name} chai is ready!")

async def main():
    await asyncio.gather(
        brew_chai("Masala chai"),
        brew_chai("Ginger chai"),
        brew_chai("Lemon chai"),
    )

asyncio.run(main())
