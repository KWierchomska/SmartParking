import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor9"
MQTT_CLIENT = "Sensor9_MQTT"

shadow = config.setupShadow(SHADOW_CLIENT)
mqttClient = config.setupMQTT(MQTT_CLIENT)

battery = 1.0
batteryWarningSent = False

while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR9",
            "latitude": 50.064170,
            "longitude": 19.943154,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": battery,
            "address": "Plac Swiętego Ducha 1, Kraków",
            "payable": True
        }
    }}

    battery = config.sendShadow(data, shadow)

    if battery <= 0.2 and not batteryWarningSent:
        config.sendMQTT(mqttClient, "SENSOR9", battery)
        batteryWarningSent = True
    if battery > 0.2:
        batteryWarningSent = False

    if battery == 0.0:
        shadow.disconnect()
        mqttClient.disconnect()
        exit(1)

    time.sleep(60)
