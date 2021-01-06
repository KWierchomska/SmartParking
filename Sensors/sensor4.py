import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor4"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR4",
            "latitude": 50.065275,
            "longitude": 19.927807,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Karmelicka 26, Kraków",
            "payable": False
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
