import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor8"
MQTT_CLIENT   = "Sensor8_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR8"
latitude      = 50.067502
longitude     = 19.940863
address       = "Rynek Kleparski 15, Kraków"
payable       = True

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
