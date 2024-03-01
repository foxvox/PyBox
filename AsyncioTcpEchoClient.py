import asyncio

async def tcp_echo_client(msg):
    reader, writer = await asyncio.open_connection('127.0.0.1', 2500)

    print('Send: %r' % msg)
    writer.write(msg.encode())

    data = await reader.read(100)
    print('Recieved: %r' % data.decode())

    print('Close the socket')
    writer.close()

msg = 'Hello World!'
loop = asyncio.new_event_loop()
loop.run_until_complete(tcp_echo_client(msg))
loop.close()