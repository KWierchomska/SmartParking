import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor5"
MQTT_CLIENT   = "Sensor5_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR5"
latitude      = 50.071929
longitude     = 19.935553
address       = "Długa 72, Kraków"
payable       = True

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
