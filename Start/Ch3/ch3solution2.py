def count_days():
    import json
    import statistics

    # open the sample weather data file and use the json module to load and parse it
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def average_temp(day):
        return (day['tmin'] + day['tmax']) / 2
    
    winter = ["-12-","-01-","-02-"]
    winter_months = [d for d in weatherdata if any([month in d['date'] for month in winter])]
    print(f"Data for {len(winter_months)} winter days")

    avg_winter_temps = [average_temp(d) for d in winter_months]
    print(max(avg_winter_temps))
    print(avg_mean := statistics.mean(avg_winter_temps))

    upper_outlier = avg_mean + (statistics.stdev(avg_winter_temps) * 2)
    print(upper_outlier)

    max_outliers = [t for t in avg_winter_temps if t >= upper_outlier]
    print(len(max_outliers))

    return 0

count_days()