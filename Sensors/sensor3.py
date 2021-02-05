import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor3"
MQTT_CLIENT   = "Sensor3_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR3"
latitude      = 50.065354
longitude     = 19.929605
address       = "Karmelicka 26, Kraków"
payable       = True

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
