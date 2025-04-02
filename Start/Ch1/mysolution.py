# Python code​​​​​​‌‌​‌​​​​‌‌​​​​​‌​‌‌​​​​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = False

import json

def get_cold_windy_rainy_days():
    # your code goes here
    # need to update the file location to get this to work
    # outside the built in code work
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    # print(weatherdata[0])
    # print(len(weatherdata))
    
    rainorsnowday = [day for day in weatherdata if day['prcp'] > 0.7 or day['snow'] > 0.7]
    # print(f'number of rain or snow days: {len(rainorsnowday)}')

    # print((weatherdata[0]['tmin'] + weatherdata[0]['tmax']) / 2)

    avgtmpday = [day for day in weatherdata if (day['tmin'] + day['tmax']) / 2 < 45]
    # print(f'number of days with avg temp below 45: {len(avgtmpday)}')
    # print(avgtmpday[:5])

    windydays = [day for day in weatherdata if isinstance(day['awnd'], (float)) and day['awnd'] > 10]
    # print(f'number of windy days: {len(windydays)}')
    # print(windydays[0])

    alldays = [day for day in weatherdata if (day['prcp'] > 0.7 or day['snow'] > 0.7) and ((day['tmin'] + day['tmax']) / 2 < 45) and (isinstance(day['awnd'], (float)) and day['awnd'] > 10)]
    # print(len(alldays))
    # print(alldays[0])

    return alldays
