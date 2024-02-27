import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))
    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()
    print("Close the client socket")
    writer.close()

loop = asyncio.new_event_loop()
# new_event_loop 사용시 start_server 4번째 인자 사용 안 함
server_coro = asyncio.start_server(handle_echo, '127.0.0.1', 2500)
task = loop.create_task(server_coro)
print('Serving...')
loop.run_forever()
