import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor7"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR7",
            "latitude": 50.066816,
            "longitude": 19.943975,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Stanisława Worcella 6, Kraków",
            "payable": False
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
