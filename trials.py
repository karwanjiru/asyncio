import asyncio

async def delayed_hi(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Hi after {seconds} seconds")

async def delayed_bye(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Bye after {seconds} seconds")

async def main():
    await asyncio.gather(
        delayed_hi(1),
        delayed_hi(5),
        delayed_bye(2),
        delayed_hi(3),
        delayed_bye(4),
    )

asyncio.run(main())