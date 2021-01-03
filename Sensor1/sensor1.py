import datetime
import json
import random
import time

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

SHADOW_CLIENT = "raspShadowClient"
HOST_NAME = "aj91jzc00agcm-ats.iot.us-east-1.amazonaws.com"
ROOT_CA = "AmazonRootCA1.pem"
PRIVATE_KEY = "3f0b7334d8-private.pem.key"
CERT_FILE = "3f0b7334d8-certificate.pem.crt"
SHADOW_HANDLER = "Sensor1"


def update_callback(payload, response_status, token):
    print()
    print('UPDATE: $aws/things/' + SHADOW_HANDLER +
          '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + response_status)
    print("token = " + token)


# Create, configure, and connect a shadow client.
raspShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
raspShadowClient.configureEndpoint(HOST_NAME, 8883)
raspShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,
                                      CERT_FILE)
raspShadowClient.configureConnectDisconnectTimeout(10)
raspShadowClient.configureMQTTOperationTimeout(5)
raspShadowClient.connect()

# Create a programmatic representation of the shadow.
myDeviceShadow = raspShadowClient.createShadowHandlerWithName(
    SHADOW_HANDLER, True)

while True:
    available = random.choice([True, False])
    data = {"state": {
        "reported": {
            "deviceID": "SENSOR1",
            "latitude": -32.8645,
            "longitude": 25.9577,
            "available": available,
            "time": str(datetime.datetime.now()),
            "battery": 0.7,
            "address": "190 Seth Ways, XYZ, A",
            "payable": True
        }
    }}
    myDeviceShadow.shadowUpdate(json.dumps(data), update_callback, 5)

    time.sleep(60)
