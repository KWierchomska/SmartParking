import random
import datetime
import time
import config

SHADOW_CLIENT = "Sensor6"
MQTT_CLIENT = "Sensor6_MQTT"

shadow = config.setupShadow(SHADOW_CLIENT)
mqttClient = config.setupMQTT(MQTT_CLIENT)

battery = 1.0
batteryWarningSent = False

while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR6",
            "latitude": 50.068665,
            "longitude": 19.940810,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": battery,
            "address": "Świętego Filipa 15, Kraków",
            "payable": True
        }
    }}

    battery = config.sendShadow(data, shadow)

    if battery <= 0.2 and not batteryWarningSent:
        config.sendMQTT(mqttClient, "SENSOR6", battery)
        batteryWarningSent = True
    if battery > 0.2:
        batteryWarningSent = False

    if battery == 0.0:
        shadow.disconnect()
        mqttClient.disconnect()
        exit(1)

    time.sleep(60)
