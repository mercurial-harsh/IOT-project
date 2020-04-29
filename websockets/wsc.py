
# WS client example

import asyncio
import websockets



id = input("What's your ID? ")
async def hello():
	uri = "ws://192.168.43.118:8765"
	choice="Y"
	global id 
	while "y"==choice.casefold():
		async with websockets.connect(uri) as websocket:
			global id
			await websocket.send(id)
			
			greeting = await websocket.recv()
			print(f"< {greeting}")
	choice=input("wish to continue(y/N) ?")

asyncio.get_event_loop().run_until_complete(hello())
#asyncio.get_event_loop().run_forever()
