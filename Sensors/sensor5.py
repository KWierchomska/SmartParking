import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor5"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR5",
            "latitude": 50.071929,
            "longitude": 19.935553,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Długa 72, Kraków",
            "payable": True
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
