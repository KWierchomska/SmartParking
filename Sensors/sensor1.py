import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor1"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR1",
            "latitude": 50.058412,
            "longitude": 19.935923,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Plac Wszystkich Świętych 5, Kraków",
            "payable": True
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
