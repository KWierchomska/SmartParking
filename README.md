# SmartParking
A project created for IoT class at AGH University of Science and Technology. It emulates the basic workings of a smart parking system, giving users the ability to discover available parking spots closest to their current location. 

Authors:
- Izabela Czajowska
- Jerzy Jędrzejaszek
- Agata Nowara
- Kinga Wierchomska

## Description

In essence, the project consists of a client app and scripts representing parking sensors. The scripts communicate their status to a database, which the client app then queries through a series of intermediaries.

Technology-wise the project is based on Amazon's web services, specifically API Gateway, DynamoDB, Lambda, the IoT Core and as well SNS. To aid with the specifics of the topic we used an extension library for DynamoDB used for managing geographic position data. The scripts representing the client app and IoT devices are written in Python.

To describe the sequence of operation in more detail:
1. After being turned on, a sensor will begin periodically sending MQTT messages to IoT Core with updates on its current status
2. These messages are forwarded to Lambda, where a dedicated handler function will update the device's status in the database. If the device is connecting for the first time, the function will create a corresponding entry in the database.
3. Eventually, a client app will make a request to find nearby parking spaces. This occurs via HTTP. The request is received by the API Gateway and forwarded to a handler function in Lambda. This function conducts the search based on client-specified parameters and replies with a set of spots that match the criteria. These are then sent back to the client as JSON in a HTTP response.
4. In case of the low battery status of specific sensor we send the notification to the administrator using Simple Notification System (SNS).

## Architecture scheme
![Architecture scheme](images/scheme.png) <br>

## Presentation

To visualize the functioning of our application we prepared a high resolution image, which is a part of Google Maps, presenting the city center of Cracow. 
On this map we present the position of user based on given coordinates and found available parking spots within the specified radius.

### Program executing
The input argumenets of our program are latitude, longitude and radius of search. Based on given data, program is sending the request to the database and receives json with the list of available parking places. <br>
![Input](images/input.png) <br>

### Visualisation
![Parking spots map](images/map.png) <br>







