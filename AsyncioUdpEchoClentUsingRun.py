import asyncio
class EchoClientProtocol:
    def __init__(self, msg, loop):
        self.msg = msg
        self.loop = loop
        self.transport = None
        self.on_con_lost = loop.create_future()

    def connection_made(self, transport):
        self.transport = transport
        print('Send: ', self.msg)
        self.transport.sendto(self.msg.encode())

    def datagram_received(self, data, addr):
        print("Received: ", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print("Connection closed")
        self.on_con_lost.set_result(True)

async def main():
    loop = asyncio.get_running_loop()

    msg = "Hello World!"
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(msg, loop), remote_addr=('127.0.0.1', 2500))

    try:
        await protocol.on_con_lost
    finally:
        transport.close()

asyncio.run(main())