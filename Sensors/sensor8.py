import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor8"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR8",
            "latitude": 50.067502,
            "longitude": 19.940863,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Rynek Kleparski 15, Kraków",
            "payable": True
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
