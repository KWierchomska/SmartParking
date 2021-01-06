import json

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

HOST_NAME = "aj91jzc00agcm-ats.iot.us-east-1.amazonaws.com"
ROOT_CA = "AmazonRootCA1.pem"
PRIVATE_KEY = "3f0b7334d8-private.pem.key"
CERT_FILE = "3f0b7334d8-certificate.pem.crt"
SHADOW_HANDLER = "Sensors"


def update_callback(payload, response_status, token):
    print()
    print('UPDATE: $aws/things/' + SHADOW_HANDLER +
          '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + response_status)
    print("token = " + token)


def setup(SHADOW_CLIENT):
    # Create, configure, and connect a shadow client.
    shadow_client = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
    shadow_client.configureEndpoint(HOST_NAME, 8883)
    shadow_client.configureCredentials(ROOT_CA, PRIVATE_KEY,
                                       CERT_FILE)
    shadow_client.configureConnectDisconnectTimeout(10)
    shadow_client.configureMQTTOperationTimeout(5)
    shadow_client.connect()

    # Create a programmatic representation of the shadow.
    return shadow_client.createShadowHandlerWithName(
        SHADOW_HANDLER, True)


def send(data,  device_shadow):
    device_shadow.shadowUpdate(json.dumps(data), update_callback, 5)
