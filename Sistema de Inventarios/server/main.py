
import json
import time
from routes.routeLogin import routeLogin
from routes.routeApp import routeApp
import threading
import asyncio

async def handle_client(reader, writer):
    data = await reader.read(1024)
    res = data.decode("utf-8")

    addr = writer.get_extra_info('peername')
    data = json.loads(res)
    print(addr)
    headType = data["Head"]["type"]
    headMode = data["Head"]["mode"]
    headTable = data["Head"]["table"]
    
    dataBody = data["Body"]
    
    if headTable == "usuario":
        sendMsg = routeLogin(dataBody)
    elif headTable == "producto":
        sendMsg = routeApp(dataBody, headMode, headType)
    else:
        sendMsg = "400 Bad Request".encode("utf-8")
    time.sleep(0)
    writer.write(sendMsg)
    await writer.drain()

    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, 'your_ip(localhost)', 8100)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        # await server.serve_forever()
        hilo = threading.Thread(target =  await server.serve_forever())
        hilo.start()
asyncio.run(main())
#     print(" [ACTIVE CONNECTIONS] " + str(threading.active_count() - 1))
