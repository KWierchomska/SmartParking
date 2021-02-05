import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor2"
MQTT_CLIENT   = "Sensor2_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR2"
latitude      = 50.055446
longitude     = 19.937351
address       = "Świętego Idziego 4, Kraków"
payable       = False

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
