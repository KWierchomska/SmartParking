import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor2"
MQTT_CLIENT = "Sensor2_MQTT"

shadow = config.setupShadow(SHADOW_CLIENT)
mqttClient = config.setupMQTT(MQTT_CLIENT)

battery = 1.0
batteryWarningSent = False

while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR2",
            "latitude": 50.055446,
            "longitude": 19.937351,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": battery,
            "address": "Świętego Idziego 4, Kraków",
            "payable": False
        }
    }}

    battery = config.sendShadow(data, shadow)

    if battery <= 0.2 and not batteryWarningSent:
        config.sendMQTT(mqttClient, "SENSOR2", battery)
        batteryWarningSent = True
    if battery > 0.2:
        batteryWarningSent = False

    if battery == 0.0:
        shadow.disconnect()
        mqttClient.disconnect()
        exit(1)

    time.sleep(60)
