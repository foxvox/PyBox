import asyncio
import time

# 비동기처리 / 동시성 프로그래밍
# event 발생 시점과 event 처리 시점이 다르다.
# evnet loop에 task를 넣어주면 각각의 task의 event 발생시점과 처리시점이 다를 수 있다.

async def say(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

# 이벤트 루프를 가져온다.
loop = asyncio.new_event_loop()

print(f"started at {time.strftime('%X')}")

# 태스크 생성
task1 = loop.create_task(say('First hello', 2))
task2 = loop.create_task(say('Second hello', 3))
# 태스크가 실행 완료될 때까지 루프 실행
loop.run_until_complete(task1)
loop.run_until_complete(task2)

print(f"finished at {time.strftime('%X')}")

loop.close()
