# SmartParking
A project created for IoT class at AGH University of Science and Technology. It emulates the basic workings of a smart parking system, giving users the ability to discover available parking spots closest to their current location. 

Authors:
- Izabela Czajowska
- Jerzy Jędrzejaszek
- Agata Nowara
- Kinga Wierchomska

## Description

Technology-wise the project is based on Amazon's web services, specifically API Gateway, DynamoDB, Lambda, the IoT Core and as well SNS. To aid with the specifics of the topic we used an extension library for DynamoDB used for managing geographic position data. The scripts representing the client app and IoT devices are written in Python.

## Architecture scheme
![Architecture scheme](images/scheme.png) <br>
## IoT Core
AWS IoT Core provides secure, bi-directional communication for Internet-connected devices (such as sensors) to connect to the AWS Cloud over MQTT, HTTPS.
#### Sensors
10 sensors have been created each of them is represented as Thing in IoT Core service. We have provided the same policy to every sensor to control many nearly identical devices.
![Architecture scheme](images/sensors.png) <br>
![Architecture scheme](images/policy.png) <br>

[GenericSensor](Sensors/GenericSensor.py) class imitates a real device which:
- connects to the service 
- publish to the **$aws/things/Sensors/shadow/update** topic data:
```json
{"state": {
                "reported": {
                    "deviceID": self.deviceID,
                    "latitude": self.latitude,
                    "longitude": self.longitude,
                    "available": available,
                    "time": str(datetime.datetime.now()),
                    "battery": self.battery,
                    "address": self.address,
                    "payable": self.payable
                }
}}
```
- publish to the **$aws/things/Sensors/battery** topic information about battery level

In summary device after being turned on, will begin periodically sending MQTT messages to IoT Core with updates on its current status.

#### Rules

Enable interacting with AWS Services. We have created 2 rules:
- insertRule which triggers Lambda function for inserting and updating information into the DynamoDB
![Architecture scheme](images/insertRule.png) <br>
  
- batteryRule which sends a message as an SNS push notification to admin e-mail, when sensor's battery level is lower than 20%
![Architecture scheme](images/batteryRule.png) <br>
  
## DynamoDB
DynamoDB is a fully managed proprietary NoSQL database. With usage of Geo Library for Amazon DynamoDB (dynamodbgeo) library we were able to make geospatial data manipulation and querying much more efficient.
All information sent from sensors were stored and updated in this database.
![Architecture scheme](images/dynamodb.png) <br>

## Simple Notification Service
Amazon Simple Notification Service (Amazon SNS) is a web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients. We have used it for notifying admin about low battery level in sensor, by sending e-mail.


## API Gateway
API Gateway provides tools for creating and documenting web APIs that route HTTP requests to Lambda functions.
We have managed to use this service for making request from client app in order to find unoccupied parking spots.
API Gateway waits for a response from function and relays the result to the caller.

  
## Lambda
It is a computing service that runs code in response to events and automatically manages the computing resources required by that code.

In our project messages which were sent by sensors are forwarded to Lambda, where a dedicated handler function [updateHandler](updateHandler.py) will update the device's status in the database. If the device is connecting for the first time, the function will create a corresponding entry in the database.

Eventually, a client app [userScript](userScript.py) will make a request to find nearby parking spaces. This occurs via HTTP. The request is received by the API Gateway and forwarded to a handler function [findParkingSpaces](findParkingSpaces.py). This function conducts the search based on client-specified parameters and replies with a set of spots that match the criteria. These are then sent back to the client as JSON in a HTTP response.

## IAM
AWS Identity and Access Management (IAM) helps define what a principal entity (person or application) is allowed to do in an account.
Access can be managed in AWS by creating policies and attaching them to IAM identities (users, groups of users, or roles) or AWS resources.
It was necessary for us to use this service in order to enable Lambda functions full access to DynamoDB and for examine debug messages in Cloud Watch.


## Presentation

To visualize the functioning of our application we prepared a high resolution image, which is a part of Google Maps, presenting the city center of Cracow. 
On this map we present the position of user based on given coordinates and found available parking spots within the specified radius.

### User program
The input arguments of our program are latitude, longitude and radius of search. Based on given data, program is sending the request to the database and receives json with the list of available parking places. <br>
![Input](images/input.png) <br>

### Visualisation
![Parking spots map](images/map.png) <br>







