import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City():
    def __init__(self, name, lat, lon):
        self.name = name
        try:
            self.lat = float(lat)
        except Exception:
            pass
        try:
            self.lon = float(lon)
        except Exception:
            pass


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

cities = []

def cityreader():
    global cities

    with open('cities.csv','r') as derp:
        cities = [City(i[0], i[3], i[4]) for i in csv.reader(derp)]
        cities.pop(0)

    return cities

cityreader()

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f'{c.name}, {c.lat}, {c.lon}')

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# lat1, lon1, lat2, lon2 = input().split(',')


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    lats = [lat1, lat2].sort()
    lons = [lon1, lon2].sort()

    for c in cities:

        if (c.lat > lats[0]) and (c.lat < lats[1]):
            if (c.lon > lons[0]) and (c.lon < lons[1]):
                within.append(c)
            else:
                pass
        else:
            pass

    return within
