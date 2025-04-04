import json

def get_day_temp_descriptions():

    # Your code goes here
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    # print(weatherdata[0])

    def day_descr(temp):
        if temp <= 60:
            return "cold"
        elif temp < 80:
            return "warm"
        else:
            return "hot"

    tuplefun = list(map(lambda a:(a['date'], day_descr((a['tmin'] + a['tmax']) / 2)), weatherdata))
    # print(tuplefun[0:5])
        
    return tuplefun