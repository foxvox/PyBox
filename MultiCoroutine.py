import asyncio
import time

# asyncio.get_event_loop 대신 asyncio.new_event_loop를 사용한다.

async def say(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

loop = asyncio.new_event_loop()

print(f"started at {time.strftime('%X')}")

# task를 만들어서 실행해야 동시성 프로그램 역할을 할 수 있다.
# 순차적으로 실행된 결과를 볼 수 있다.

loop.run_until_complete(say('First hello', 2))
loop.run_until_complete(say('Second hello', 3))

print(f"finished at {time.strftime('%X')}")

loop.close()