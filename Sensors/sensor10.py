import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor10"
MQTT_CLIENT = "Sensor10_MQTT"

shadow = config.setupShadow(SHADOW_CLIENT)
mqttClient = config.setupMQTT(MQTT_CLIENT)

battery = 1.0
batteryWarningSent = False

while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR10",
            "latitude": 50.063419,
            "longitude": 19.941958,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": battery,
            "address": "Szpitalna 30, Kraków",
            "payable": False
        }
    }}

    battery = config.sendShadow(data, shadow)

    if battery <= 0.2 and not batteryWarningSent:
        config.sendMQTT(mqttClient, "SENSOR10", battery)
        batteryWarningSent = True
    if battery > 0.2:
        batteryWarningSent = False

    if battery == 0.0:
        shadow.disconnect()
        mqttClient.disconnect()
        exit(1)

    time.sleep(60)
