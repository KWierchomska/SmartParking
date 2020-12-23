# Generated from IOT demo series here: https://www.youtube.com/watch?v=RJ1R0cLx0Fs
# program to simulate some data on AWS IOT
# Make sure you have "AWSIoTPythonSDK" installed before runing this script.
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import random, time

# replace with the right certificates from  AWS IOT
SHADOW_CLIENT = "raspShadowClient"
HOST_NAME = "aj91jzc00agcm-ats.iot.us-east-1.amazonaws.com"
ROOT_CA = "AmazonRootCA1.pem"
PRIVATE_KEY = "3f0b7334d8-private.pem.key"
CERT_FILE = "3f0b7334d8-certificate.pem.crt"
SHADOW_HANDLER = "Sensor1"


def myShadowUpdateCallback(payload, responseStatus, token):
    print()
    print('UPDATE: $aws/things/' + SHADOW_HANDLER +
          '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + responseStatus)
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

# Keep generating random test data until this scrip stops running.
# To stop running this script, press Ctrl+C.

while True:
    # Generate random True or False test data to represent
    # okay or low available levels, respectively.

    print("--------------------------")
    available = random.choice([True, False])
    # print(available)
    if available:
        myDeviceShadow.shadowUpdate(
            '{"state":{"reported":{"available":"true"}}}',
            myShadowUpdateCallback, 5)
    else:
        myDeviceShadow.shadowUpdate(
            '{"state":{"reported":{"available":"false"}}}',
            myShadowUpdateCallback, 5)

    # Wait for this test value to be added.
    # sleep 60 seconds
    time.sleep(60)
