import asyncio

async def tcp_echo_client(msg):
    reader,writer = await asynci.open_connection('127.0.0.1',8888)

    print(f'send:{msg}')
    writer.write(msg.encode())
    await writer.drain()

    print("waiting for server response...")
    data = await reader.read(100)
    print(f"received : {data.decode()}")

    print('closing the connnection')
    writer.close()
    await writer.wait_closed()

async def main():
    await tcp_echo_client("hello , server!")

asyncio.run(main())