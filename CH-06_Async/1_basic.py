import asyncio
import time

#Coroutine function
async def main():
    print("Hello")
    await asyncio.sleep(3)
    print("World")

#Run the main coroutine
asyncio.run(main())