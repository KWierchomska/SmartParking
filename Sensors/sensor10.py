import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor10"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR10",
            "latitude": 50.063419,
            "longitude": 19.941958,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Szpitalna 30, Kraków",
            "payable": False
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
