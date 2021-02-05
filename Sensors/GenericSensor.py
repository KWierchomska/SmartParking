import random
import datetime
import time
import config


class GenericSensor:

    def __init__(self, shadow, mqttClient, battery, deviceID, latitude, longitude, address, payable):
        self.shadow = shadow
        self.mqttClient = mqttClient
        self.battery = battery
        self.deviceID = deviceID
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.payable = payable

    def run(self):
        batteryWarningSent = False

        while True:
            available = random.choice([True, False])
            data = {"state": {
                "reported": {
                    "deviceID": self.deviceID,
                    "latitude": self.latitude,
                    "longitude": self.longitude,
                    "available": available,
                    "time": str(datetime.datetime.now()),
                    "battery": self.battery,
                    "address": self.address,
                    "payable": self.payable
                }
            }}

            self.battery = config.sendShadow(data, self.shadow)

            if self.battery <= 0.2 and not batteryWarningSent:
                config.sendMQTT(self.mqttClient, "SENSOR1", self.battery)
                batteryWarningSent = True
            if self.battery > 0.2:
                batteryWarningSent = False

            if self.battery == 0.0:
                self.shadow.disconnect()
                self.mqttClient.disconnect()
                exit(1)

            time.sleep(60)
