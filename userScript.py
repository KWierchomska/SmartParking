import requests
import geopy.distance
import time

URL = "https://8oweaskc5f.execute-api.us-east-1.amazonaws.com/test/queries"
params = {"lat":  0, "long": 0, "radius": 100}

while True:
    print("Enter latitude:")
    lat = input()
    print("Enter longitude:")
    long = input()
    print("Enter radius of search:")
    radius = input()

    params["lat"] = float(lat)
    params["long"] = float(long)
    params["radius"] = float(radius)

    response = requests.get(URL, params).json()

    print("Available parking spots:\n")
    for it, el in enumerate(response["result"]):
        c1 = (lat, long)
        c2 = (el["geoJson"]["S"])
        dist = geopy.distance.distance(c1,c2).km
        print(str(it) + " latitude,longitude: " + el["geoJson"]["S"] + "; distance: " + str(dist))

    #time.sleep(10)
