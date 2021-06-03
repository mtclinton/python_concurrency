import asyncio


async def f():
    return 123

coro = f()
try:
    coro.send(None)
except StopIteration as e:
    print("The answer was: ", e.value)

async def g():
    await asyncio.sleep(1.0)
    return 1234

async def main():
    result = await g()
    print(result)

asyncio.run(main())