import asyncio
import websockets

async def hello():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        name = input("what is your name? ")

        await websocket.send(name)
        print(f'client sent {name}')

        # Get the received info from server and assign it to greeting
        greeting = await websocket.recv()
        print(f'client recieved {greeting}')

if __name__ == "__main__":
    asyncio.run(hello())