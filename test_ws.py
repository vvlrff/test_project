import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8000/bot/send_bot"

    try:
        async with websockets.connect(uri) as websocket:
            message = "Hello, WebSocket!"
            await websocket.send(message)
            print(f"Sent message: {message}")

            response = await websocket.recv()
            print(f"Received response: {response}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"ConnectionClosedError: {e}")

asyncio.get_event_loop().run_until_complete(send_message())