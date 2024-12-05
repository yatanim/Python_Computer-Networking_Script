import asyncio

async def handle_client(reader,writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr}")

    while True:
        data = await reader.read(100)
        msg = data.decode()
        if not data:
            break
        print(f"Received {msg} from {addr}")
        writer.write(data)
        await writer.drain()
    print(f"closing the connection to {addr}")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_servr(handle_client,'127.0.0.1',8888)
    addr = server.sockets[0].getsocketname()
    print(f"serving on {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(main())