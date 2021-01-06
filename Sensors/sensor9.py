import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor9"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR9",
            "latitude": 50.064170,
            "longitude": 19.943154,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Plac Swiętego Ducha 1, Kraków",
            "payable": True
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
