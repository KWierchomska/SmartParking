import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor3"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR3",
            "latitude": 50.065354,
            "longitude": 19.929605,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Karmelicka 26, Kraków",
            "payable": True
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
