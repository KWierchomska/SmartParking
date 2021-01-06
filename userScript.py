import requests
import geopy.distance
import time
import matplotlib.pyplot as plt

URL = "https://8oweaskc5f.execute-api.us-east-1.amazonaws.com/test/queries"
params = {"lat":  0, "long": 0, "radius": 100}

ruh_m = plt.imread('./high_resolution_image.png')

MAP_LONG_MIN = 19.918226
MAP_LONG_MAX = 19.973078
MAP_LAT_MIN = 50.050085
MAP_LAT_MAX = 50.085449

# Boundary Box of the map file high_resolution_image.png
BBox = (MAP_LONG_MIN, MAP_LONG_MAX, MAP_LAT_MIN, MAP_LAT_MAX)

# Example latitude, longitude arrays
LATITUDE_ARR = []       # [50.06477478214624, 50.062690310916075, 50.05767280893131, 50.05571219152061, 50.05862094762662]
LONGITUDE_ARR = []      # [19.93192798675469, 19.931092082082436, 19.9307177912443, 19.942482360328277, 19.945385956102193]
# Point color array
COLORS = []               # ['b' for _ in LONGITUDE_ARR]

while True:
    print("Enter latitude:")
    lat = input()
    print("Enter longitude:")
    long = input()
    print("Enter radius of search:")
    radius = input()
    # Example values: 50.066178137497, 19.936686213350587

    params["lat"] = float(lat)
    params["long"] = float(long)
    params["radius"] = float(radius)

    LATITUDE_ARR.append(float(lat))
    LONGITUDE_ARR.append(float(long))
    COLORS.append('r')

    response = requests.get(URL, params).json()

    print("Available parking spots:\n")
    for it, el in enumerate(response["result"]):
        c1 = (lat, long)
        c2 = (el["geoJson"]["S"])
        dist = geopy.distance.distance(c1,c2).km
        print(str(it) + " latitude,longitude: " + el["geoJson"]["S"] + "; distance: " + str(dist) + " address: " + el["address"]["S"])

        # TODO: Check (Add latitude, longitude to arrays + set color of new point)
        # Add parking spot to list
        point = el["geoJson"]["S"].split(",")
        LATITUDE_ARR.append(float(point[0]))
        LONGITUDE_ARR.append(float(point[1]))
        COLORS.append('b')

    # Draw Plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(LONGITUDE_ARR, LATITUDE_ARR, zorder=1, alpha=0.7, c=COLORS, s=175)

    ax.set_title('Available Parking Spots')

    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    # ax.set_aspect('equal', 'box')

    ax.imshow(ruh_m, zorder=0, extent=BBox, aspect='equal')

    # Zoom area where parking spots are
    ax.set_xlim(min(LONGITUDE_ARR) - 0.005, max(LONGITUDE_ARR) + 0.005)
    ax.set_ylim(min(LATITUDE_ARR) - 0.005, max(LATITUDE_ARR) + 0.005)
    plt.show()
    #time.sleep(10)
