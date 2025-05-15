import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

def bad_data(d):
    return not isinstance(d['awnd'], float)

bdata = list(filter(bad_data, weatherdata))

pprint.pprint(bdata)