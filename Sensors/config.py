import json

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient, AWSIoTMQTTClient

ENDPOINT = "aj91jzc00agcm-ats.iot.us-east-1.amazonaws.com"
ROOT_CA = "AmazonRootCA1.pem"
PRIVATE_KEY = "3f0b7334d8-private.pem.key"
CERT_FILE = "3f0b7334d8-certificate.pem.crt"
SHADOW_HANDLER = "Sensors"

TOPIC = "$aws/things/" + SHADOW_HANDLER + "/battery"


def update_callback(payload, response_status, token):
    print()
    print('UPDATE: $aws/things/' + SHADOW_HANDLER +
          '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + response_status)
    print("token = " + token)


def setupShadow(SHADOW_CLIENT):
    # Create, configure, and connect a shadow client.
    shadow_client = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
    shadow_client.configureEndpoint(ENDPOINT, 8883)
    shadow_client.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
    shadow_client.configureConnectDisconnectTimeout(10)
    shadow_client.configureMQTTOperationTimeout(5)
    shadow_client.connect()

    # Create a programmatic representation of the shadow.
    return shadow_client.createShadowHandlerWithName(SHADOW_HANDLER, True)


def setupMQTT(CLIENT_ID):
    myAWSIoTMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
    myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
    myAWSIoTMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
    myAWSIoTMQTTClient.connect()
    return myAWSIoTMQTTClient


def sendShadow(data, device_shadow):
    newBattery = data["state"]["reported"]["battery"] - 0.1
    device_shadow.shadowUpdate(json.dumps(data), update_callback, 5)
    return max(newBattery, 0.0)


def sendMQTT(deviceMQTTClient, deviceId, battery):
    print("\nSending battery alert...")
    data = "Alert: low battery on device " + deviceId + ", battery level: " + str(battery)
    deviceMQTTClient.publish(TOPIC, json.dumps(data), 0)
    print("Alert sent!\n")
