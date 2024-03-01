import asyncio

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
    def data_receiveved(self, _data):
        message = _data.decode()
        print('Data received: {!r}'.format(message))
        print('Send: {!r}'.format(message))
        self.transport.write(_data)

        # print('Close the client socket')
        # self.transport.close()
async def main():
    loop = asyncio.get_event_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(), '127.0.0.1', 2500)

    async with server:
        await server.serve_forever()

asyncio.run(main())