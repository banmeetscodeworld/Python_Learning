
#async api call
import asyncio

async def api_call(url:str, delay:int):
    await asyncio.sleep(delay)
    print("data fetched from",url)
    return f"{url} data"

async def main():
    tasks = await asyncio.gather(
        api_call("https://api1.com", 2),
        api_call("https://api2.com", 3),
        api_call("https://api3.com", 1)
    )

    #Another way to create tasks with list comprehension
    #tasks = [api_call(url, delay) for url, delay in [("https://api1.com", 2), ("https://api2.com", 3), ("https://api3.com", 1)]]
    #results = await asyncio.gather(*tasks)

    print("All tasks completed:", tasks)
asyncio.run(main())