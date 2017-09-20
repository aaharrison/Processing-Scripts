import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import datetime
from datetime import date, timedelta

def test(r25, banner):
    
    # Format R25 Data Types
    df = r25.copy()
    df["CRSE"] = df["CRSE"].apply(lambda x: str(x))
    df["BUILDING"] = df["BUILDING"].apply(lambda x: str(x))
    df["BUILDING"] = df["BUILDING"].apply(lambda x: x.replace(" ", ""))
    df["ROOM"] = df["ROOM"].apply(lambda x: str(x))
    df["ROOM"] = df["ROOM"].apply(lambda x: x.replace(" ", ""))

    # Format Banner Data Types
    df2 = banner.copy()
    df2["Crse"] = df2["Crse"].apply(lambda x: str(x))
    df2["Bldg1"] = df2["Bldg1"].apply(lambda x: str(x))
    df2["Room1"] = df2["Room1"].apply(lambda x: str(x))
    
    # Day of Week Translation dictionary1`
    dow = {
        "MO": 0,
        "TU": 1,
        "WE": 2,
        "TH": 3,
        "FR": 4,
        "SA": 5,
        "SU": 6
    }
    
    # Add try and except clause to handle when values have already been changed
    df["DAYS"] = df["DAYS"].apply(lambda x: x.split(" "))

    # Add try and except clause to handle when values have already been changed
    dayList = []
    for list in df["DAYS"]:
        days = []
        for x in list:
            days.append(dow[x])

        dayList.append(days)

    df["DAYS"] = dayList

    
    holder = pd.DataFrame(columns = ["Date", "Course", "Building", "Room", "Capacity"], index = [])
    
    for course, building, room, start, end, days, capacity in zip(df["CRSE"], df["BUILDING"], df["ROOM"], 
                                                       df["START_DT"], df["END_DT"], df["DAYS"], df["MAX_CAPACITY"]):
        
        classDay = []
        
        d1 = start.date()
        d2 = end.date()
        delta = d2 - d1
        
        for x in range(delta.days + 1):
            date = d1 + timedelta(days = x)
            if date.weekday() in days:
                classDay.append(date)
            else:
                pass
         
        classDF = pd.DataFrame(data = classDay, columns = ["Date"])
        
        classDF["Course"] = course
        classDF["Building"] = building
        classDF["Room"] = room
        classDF["Capacity"] = capacity
        classDF["Start Time"] = start.time()
        classDF["End Time"] = end.time()
        
        startDateTime = []
        endDateTime = []
        
        for date, start, end in zip(classDF["Date"], classDF["Start Time"], classDF["End Time"]):
            startDateTime.append(datetime.datetime.combine(date, start))
            endDateTime.append(datetime.datetime.combine(date, end))
            
        classDF["Start Time"] = startDateTime
        classDF["End Time"] = endDateTime
        
        holder = pd.concat([holder, classDF], axis = 0)
    
    holder.reset_index(inplace = True)
    holder.drop("index", axis = 1, inplace = True)
    
    holder = holder.merge(df2[["Crse", "Bldg1", "Room1", "Enrolled", "Class Maximum", "Title"]], how = "left", 
                 left_on = ["Course", "Building", "Room"], right_on = ["Crse", "Bldg1", "Room1"])
    
    holder.drop(["Date", "Crse", "Bldg1", "Room1"], axis = 1, inplace = True)
    
    holder = holder[["Start Time", "End Time", "Course", "Title", "Building", "Room", "Capacity", 
                     "Class Maximum", "Enrolled"]]
    
    holder.sort_values("Start Time", ascending = True, inplace = True)
    
    holder.reset_index(inplace = True)
    
    holder.drop("index", axis = 1, inplace = True)
    
    return(holder)