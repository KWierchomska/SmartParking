import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor1"
MQTT_CLIENT   = "Sensor1_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR1"
latitude      = 50.058412
longitude     = 19.935923
address       = "Plac Wszystkich Świętych 5, Kraków"
payable       = True

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
