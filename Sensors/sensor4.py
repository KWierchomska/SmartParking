import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor4"
MQTT_CLIENT   = "Sensor4_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR4"
latitude      = 50.065275
longitude     = 19.927807
address       = "Karmelicka 26, Kraków"
payable       = False

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
