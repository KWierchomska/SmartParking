import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor2"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR2",
            "latitude": 50.055446,
            "longitude": 19.937351,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Świętego Idziego 4, Kraków",
            "payable": False
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
