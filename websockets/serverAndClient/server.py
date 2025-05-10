import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f'Server recieved {name}') 
    greeting = f'hello {name}!'

    await websocket.send(greeting)
    print(f'Server sent {greeting}')

async def main():
    # Serve the client with the function hello
    # serve on localhost with port 8765 is a common port for websockets
    async with websockets.serve(hello, "localhost",8765): 
        await asyncio.Future() # Run main forever

# if running this file call the main func
if __name__ == "__main__":
    asyncio.run(main())