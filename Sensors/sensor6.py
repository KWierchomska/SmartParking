import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor6"

shadow = config.setup(SHADOW_CLIENT)
while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR6",
            "latitude": 50.068665,
            "longitude": 19.940810,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "Świętego Filipa 15, Kraków",
            "payable": True
        }
    }}
    config.send(data, shadow)
    time.sleep(60)
