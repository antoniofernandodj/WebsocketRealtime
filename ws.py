import json
import asyncio
import websockets
from pprint import pprint as print

clientes = []

async def send_message(message):
    for cliente in clientes:
        await cliente.send(message)

async def new_cliente_connected(socket, path):
    print('Cliente connectado')
    clientes.append(socket)
    
    while True:
        msg = await socket.recv()
        cliente_id = str(socket.id)
        data = json.dumps({'id': cliente_id, 'data': msg})
        print(data)
        await send_message(data)

async def start_server():
    async with websockets.serve(new_cliente_connected, 'localhost', 8765):
        print("Servidor iniciado na porta 8765.")

        await asyncio.Future() 


asyncio.run(start_server())
