import config
from GenericSensor import GenericSensor

SHADOW_CLIENT = "Sensor7"
MQTT_CLIENT   = "Sensor7_MQTT"
shadow        = config.setupShadow(SHADOW_CLIENT)
mqttClient    = config.setupMQTT(MQTT_CLIENT)

initBattery   = 0.25
deviceID      = "SENSOR7"
latitude      = 50.066816
longitude     = 19.943975
address       = "Stanisława Worcella 6, Kraków"
payable       = False

sensorInstance = GenericSensor(shadow, mqttClient, initBattery, deviceID, latitude, longitude, address, payable)
sensorInstance.run()
