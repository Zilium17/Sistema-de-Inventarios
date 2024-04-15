import asyncio
import json
async def request(host, port, message):
    reader, writer = await asyncio.open_connection(host, port)
    message = json.dumps(message)
    writer.write(message.encode('utf-8'))
    await writer.drain()
    data = await reader.read(4096)
    response = data.decode("utf-8")
    writer.close()
    await writer.wait_closed()
    return response