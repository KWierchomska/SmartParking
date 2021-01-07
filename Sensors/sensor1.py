import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor1"
MQTT_CLIENT = "Sensor1_MQTT"

shadow = config.setupShadow(SHADOW_CLIENT)
mqttClient = config.setupMQTT(MQTT_CLIENT)

battery = 0.25
batteryWarningSent = False

while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR1",
            "latitude": 50.058412,
            "longitude": 19.935923,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": battery,
            "address": "Plac Wszystkich Świętych 5, Kraków",
            "payable": True
        }
    }}

    battery = config.sendShadow(data, shadow)

    if battery <= 0.2 and not batteryWarningSent:
        config.sendMQTT(mqttClient, "SENSOR1", battery)
        batteryWarningSent = True
    if battery > 0.2:
        batteryWarningSent = False

    if battery == 0.0:
        shadow.disconnect()
        mqttClient.disconnect()
        exit(1)

    time.sleep(60)
