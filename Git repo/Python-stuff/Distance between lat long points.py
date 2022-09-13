from math import cos,radians,sin,acos,asin,sqrt
from function import *
"""
FORMULA TO CALCULATE 
a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
c = 2 ⋅ atan2( √a, √(1−a) )
d = R ⋅ c
where 	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km)
"""
#Delta of lat can be written as (lat2-lat1) and same goes for longitude
#Ask use to enter lattitude and longitude twice and compare using formula



def distance_calc():
    while True:
        try:
            lat1 = input("Enter the latitude of point 1:")
            if float(lat1):
                lat1 = float(lat1)
                lat1 = radians(lat1)
                break
        except ValueError:
            print("Please enter a valid point!")
    while True:
        try:
            long1 = input("Enter the longitude of point 1:")
            if float(long1):
                long1 = float(long1)
                long1 = radians(long1)
                break
        except ValueError:
            print("Please enter a valid point!")
    while True:
        try:
            lat2 = input("Enter the latitude of point 2:")
            if float(lat2):
                lat2 = float(lat2)
                lat2 = radians(lat2)
                break
        except ValueError:
            print("Please enter a proper point!")
    while True:
        try:
            long2 = input("Enter the longitude of point 2:")
            if float(long2):
                long2 = float(long2)
                long2 = radians(long2)
                break
        except ValueError:
            print("Please enter a valid point!")
    dlat = lat2 - lat1
    dlong = long2 - long1
    r = 2*6378.1
    c = (sin(dlat/2)**2) + ((cos(lat1)*cos(lat2))*(sin(dlong/2)**2))
    d = r*asin(sqrt(c))
    return d
distance = distance_calc()
print(f"The distance between the two given points are {distance} K.M")
"""
The actual part of calculating distance works fine
work on getting input and processing it
that is raise valueerror if a wrong point is inputted
Suggest create a function for it and call it to make the flow easier
"""