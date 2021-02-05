import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor10"
MQTT_CLIENT   = "Sensor10_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR10"
latitude      = 50.063419
longitude     = 19.941958
address       = "Szpitalna 30, Kraków"
payable       = False

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
