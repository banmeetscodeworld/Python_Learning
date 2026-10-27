#import time
#normal syn fn
#def api_call():
   # time.sleep(3)
   # return "orders data"

#def execute():
  #  print("executing api call")
  #  result = api_call()
  #  print("data fetched:", result)

#execute()

#async api call
import asyncio

async def api_call():
    await asyncio.sleep(3)
    return "orders data"

async def execute():
    print("executing api call")
    #if we'll not write await, error will be raised because api_call is an async function
    #it should print next statement only after api_call is completed
    result = await api_call()
    print("data fetched:", result)

asyncio.run(execute())