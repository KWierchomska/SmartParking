import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor9"
MQTT_CLIENT   = "Sensor9_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR9"
latitude      = 50.064170
longitude     = 19.943154
address       = "Plac Swiętego Ducha 1, Kraków"
payable       = True

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
