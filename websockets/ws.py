#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import requests
import json




async def hello(websocket, path):
    iotId = await websocket.recv()
    print(iotId)
      
    response=requests.get(f"https://us-central1-iot-upes.cloudfunctions.net/webhookNew/iots/{iotId}")
    
        
    if response.status_code == 200 :

        data=response.json()
        state=data["status"]
    else :
            
        state="wait a second"
    
     

    await websocket.send(state)
    #print(f"> {greeting}")

start_server = websockets.serve(hello, "192.168.43.118", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
