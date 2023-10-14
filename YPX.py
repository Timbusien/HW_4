import time
def sync_traffic_light():
    while True:
        print("Красный")
        time.sleep(5)
        print("Желтый")
        time.sleep(2)
        print("Зеленый")
        time.sleep(5)

sync_traffic_light()

import asyncio

async def async_traffic():
    while True:
        print("Красный")
        await asyncio.sleep(5)
        print("Желтый")
        await asyncio.sleep(2)
        print("Зеленый")
        await asyncio.sleep(5)

loop = asyncio.get_event_loop()
loop.run_until_complete(async_traffic())

import threading
import time

def sync_light():
    while True:
        print("Красный")
        time.sleep(5)
        print("Желтый")
        time.sleep(2)
        print("Зеленый")
        time.sleep(5)

thread = threading.Thread(target=sync_light)
thread.start()