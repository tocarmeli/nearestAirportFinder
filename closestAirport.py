import json
from sys import exit
from math import radians, cos, sin, asin, sqrt
import pandas as pd

airports = json.loads(open('airports.json').read())

zip_codes = pd.read_csv("zip_code_database.csv", sep=",")
zip_codes = zip_codes[["zip", "primary_city", "state", "latitude", "longitude", "country"]]



my_zip = int(input("Enter your zip code: "))

def distance(latZip, longZip, latAirport, longAirport):
    latZip = radians(latZip)
    latAirport = radians(latAirport)
    longZip = radians(longZip)
    longAirport = radians(longAirport)

    dLong = longAirport - longZip
    dLat = latAirport - latZip
    a = sin(dLat / 2) ** 2 + cos(latZip) * cos(latAirport) * sin(dLong / 2) ** 2

    c = 2 * asin(sqrt(a))

    radius = 6371

    return(c * radius)

found = False
zip_latitude = 0
zip_longitude = 0
for index, row in zip_codes.iterrows():
    if row["zip"] == my_zip:
        print(row)
        user_conf = input("Is this your location? Y/N: ")
        if user_conf.lower() == "y":
            zip_latitude = float(row["latitude"])
            zip_longitude = float(row["longitude"])
            found = True
if not found:
    print("Couldn't find zip code")
    exit()
print("Zip code found")

min_distance = float("inf")
closest_airport = ""

for current_airport in airports:
    if current_airport["type"] != "Airports":
        continue
    airport_latitude = float(current_airport["lat"])
    airport_longitude = float(current_airport["lon"])
    current_distance = distance(zip_latitude, zip_longitude, airport_latitude, airport_longitude)
    if current_distance < min_distance:
        # We found a closer airport. Update distance and remember airport
        min_distance = current_distance
        closest_airport = [current_airport["name"], current_airport["city"], current_airport["state"], current_airport["country"], current_airport["code"]]

print("The closest airport is: ")
print(closest_airport)
print("With a distance of " + str(min_distance))

"""
for zip in zip_codes.iteritems():
    if zip == user_location:
        print("Your city is ")
        
"""

"""
for code in zip_codes:
	if user_location in zip_codes:
		confLocation = input("Do you live in " + )


for airport in airports:
	latitude = airports
	"""