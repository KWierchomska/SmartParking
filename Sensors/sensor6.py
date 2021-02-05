import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor6"
MQTT_CLIENT   = "Sensor6_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR6"
latitude      = 50.068665
longitude     = 19.940810
address       = "Świętego Filipa 15, Kraków"
payable       = True

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
