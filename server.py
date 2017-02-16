#!/usr/bin/env python3

from ensure_venv import ensure_venv
ensure_venv(python='python3', requirements='requirements.txt')

import asyncio
import websockets

async def hello(websocket, path):
    while True:
        name = await websocket.recv()
        print('< {}'.format(name))
        greeting = 'Hello {}!'.format(name)
        await websocket.send(greeting)
        print('> {}'.format(greeting))

def main():
    start_server = websockets.serve(hello, 'localhost', 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()
