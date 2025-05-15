import json
import pprint
import random

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# build a list of the summer days in 2019
def select_days(year, month):

    # year = "2021"
    # month = "12"

    def is_summer_day(d):
        the_month = [str(year) + "-" + str(month) + "-"]
        # print(the_month)
        if any([m in d['date'] for m in the_month]):
            return True
        return False
    the_days = list(filter(is_summer_day, weatherdata))
    # pprint.pp(the_days)
    # return the_days

    # TODO: choose 5 random days from that month
    rnd_days = random.sample(the_days, k=5)
    pprint.pp(rnd_days)

select_days(2020, 12)


