import json
from functools import reduce

def miserable_day():
    # use this to work with the local json file
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    
    # with open("deps/sample-weather-history.json", "r") as weatherfile:
    #     weatherdata = json.load(weatherfile)

    def most_miserable_day(acc, elem):
        if isinstance(elem['awnd'], (float)) and isinstance(acc['awnd'], (float)):
            misery_score_elem = (elem['awnd'] + elem['prcp'] * 10 + elem['tmax'] * 0.8) / 3
            misery_score_acc = (acc['awnd'] + acc['prcp'] * 10 + acc['tmax'] * 0.8) / 3
        else:
            misery_score_elem = 0
            misery_score_acc = 0
        
        return elem if misery_score_elem > misery_score_acc else acc

    # define a "zero" value start date for the reduce function to start with
    start_val = {
        "date": "1900-01-01",
        "tmin": 0,
        "tmax": 0,
        "prcp": 0.0,
        "snow": 0.0,
        "snwd": 0.0,
        "awnd": 0.0
    }

    result = reduce(most_miserable_day, weatherdata, start_val)
    # print(result)

    return result