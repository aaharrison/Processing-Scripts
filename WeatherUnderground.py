import os
import requests
import datetime
from datetime import date, timedelta
import numpy as np
import pandas as pd


#enter start and end dates in date(Year, Month, Day) format, make sure key and site variables are set
def weatherData(start, end):
    dateRange = []
    date1 = start
    date2 = end

    delta = date2 - date1

    for x in range(delta.days + 1):
        dateRange.append((date1 + timedelta(days = x)).strftime("%Y%m%d"))
        
    data = {}
    
    for date in dateRange:
        urlstart = "http://api.wunderground.com/api/" + str(key) + "/history_"
        urlend = "/q/pws:" + str(site) + ".json"

        url = urlstart + date + urlend

        data[date] = requests.get(url).json()

        
    weatherPretty = []
    weatherYear = []
    weatherMonth = []
    weatherDay = []
    weatherHour = []
    weatherMinute = []
    weatherTemp = []
    weatherHum = []
    weatherRainRate = []
    weatherSolar = []

    for x in dateRange:
        for y in range(400):
            try:
                weatherPretty.append(data[x]["history"]["observations"][y]["date"]["pretty"])
                weatherYear.append(data[x]["history"]["observations"][y]["date"]["year"])
                weatherMonth.append(data[x]["history"]["observations"][y]["date"]["mon"])
                weatherDay.append(data[x]["history"]["observations"][y]["date"]["mday"])
                weatherHour.append(data[x]["history"]["observations"][y]["date"]["hour"])
                weatherMinute.append(data[x]["history"]["observations"][y]["date"]["min"])
                weatherTemp.append(data[x]["history"]["observations"][y]["tempi"])
                weatherHum.append(data[x]["history"]["observations"][y]["hum"])
                weatherRainRate.append(data[x]["history"]["observations"][y]["precip_ratei"])
                weatherSolar.append(data[date]["history"]["observations"][y]["solarradiation"])
            except:
                break
    
    
    weatherData = pd.DataFrame(
        data = [weatherYear, weatherMonth, weatherDay, weatherHour, weatherMinute, weatherTemp, weatherHum, weatherRainRate, weatherSolar]
    ).T
    


    weatherData.columns = ["Year","Month", "Day", "Hour", "Minute", "Temp", "RH%", "Rain Rate", "Solar Rad"]
    
    def tryFloat(x):
        try:
            return(float(x))
        except:
            return(x)

    def tryInt(x):
        try:
            return(int(x))
        except:
            return(x)
    

    weatherData["Year"] = weatherData["Year"].apply(lambda x: tryInt(x))    
    weatherData["Month"] = weatherData["Month"].apply(lambda x: tryInt(x))
    weatherData["Day"] = weatherData["Day"].apply(lambda x: tryInt(x))
    weatherData["Hour"] = weatherData["Hour"].apply(lambda x: tryInt(x))
    weatherData["Minute"] = weatherData["Minute"].apply(lambda x: tryInt(x))
    weatherData["Temp"] = weatherData["Temp"].apply(lambda x: tryFloat(x))
    weatherData["RH%"] = weatherData["RH%"].apply(lambda x: tryInt(x))
    weatherData["Rain Rate"] = weatherData["Rain Rate"].apply(lambda x: tryFloat(x))
    weatherData["Solar Rad"] = weatherData["Solar Rad"].apply(lambda x: tryFloat(x))
    

    weatherData["Date/Time"] = pd.to_datetime(weatherData[["Year", "Month", "Day", "Hour", "Minute"]])

    weatherData.set_index("Date/Time", inplace = True)
    
    weatherData = pd.DataFrame(weatherData)
    
    weatherData.to_csv("Weather Underground Output.csv", index = True)

############################################# START HERE #####################################################
# Specify API Call Parameters
key = "0bfa64942618d5ec"
site = "IGUAM5"
start = date(2017, 9, 15)
end = date(2017, 9, 18)

# Run Function

weatherData(start, end)


