import asyncio
import time
async def say(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

loop = asyncio.get_event_loop()

print(f"started at {time.strftime('%X')}")
loop.run_until_complete(say('First hello', 2))
loop.run_until_complete(say('Second hello', 3))
print(f"finished at {time.strftime('%X')}")

loop.close()