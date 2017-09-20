import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import datetime
from datetime import date, timedelta

# df --->
# RangeIndex: 40014 entries, 0 to 40013
# Data columns (total 17 columns):
# Room ID                      40014 non-null object
# Day of Week                  40014 non-null object
# Hour                         40014 non-null int64
# Class capacity               39936 non-null float64
# Class Hours Percentage       9340 non-null float64
# Class Enrollment             9340 non-null float64
# Building ID                  40014 non-null object
# Building Description         40014 non-null object
# Room Floor                   40014 non-null int64
# Room Net Sqft                40014 non-null float64
# Room Code                    40014 non-null object
# Building-Room                40014 non-null object
# Location Type ID             40014 non-null object
# Location Type Description    40014 non-null object
# Location Owner               40014 non-null object
# lat                          38376 non-null float64
# long                         38376 non-null float64
# dtypes: float64(6), int64(2), object(9)
# memory usage: 5.2+ MB

pd.read_csv()

def visualization(df, location = "BILGER HALL"):
    holder = df[df["Building Description"] == location].copy()
    try:
    
        # Update the day of the week column
        dow = {
            "F": "Friday",
            "M": "Monday",
            "T": "Tuesday",
            "W": "Wednesday",
            "R": "Thursday",
            "S": "Saturday"}

        holder["Day of Week"] = holder["Day of Week"].apply(lambda x: dow[x])
    
    except:
        pass
    
    # Create Enrollment Hours Column 
    enrollHours = []
    for enroll, hour in zip(holder["Class Enrollment"], holder["Class Hours Percentage"]):
        if (pd.isnull(enroll)) or (pd.isnull(hour)):
            enrollHours.append(np.nan)
        else:
            enrollHours.append(enroll * hour)
    
    holder["Enrollment Hours"] = enrollHours
    
    # Plot Occupancy by Day and Hour
    plt.style.use("seaborn-whitegrid")
    occupancyFigure = plt.figure(figsize = (18,10))
    occupancyAxes = occupancyFigure.add_axes([0,0,1,1])
    occupancyAxes.set_title("Average Occupancy Rate by Date", fontsize = 20)
    occupancyAxes.set_xlabel("Time of Day")
    occupancyAxes.set_ylabel("Average Occupancy %")
    occupancyAxes.set_ylim([0,1.2])
    occupancyAxes.set_xlim([0,23])
    plt.xticks(np.arange(0, 24, 1.0))     
    
    colors = ["#e74c3c", "#34495e", "#2ecc71", "#9b59b6", "#3498db", "#95a5a6"]

    occAvg = []
    n = 0
    for day in holder["Day of Week"].unique().tolist():
        dailyOccupancy = holder[holder["Day of Week"] == day].groupby("Hour")["Class Hours Percentage"].mean()
        dailyOccupancy = pd.DataFrame(data = dailyOccupancy, index = np.arange(0,24).tolist()).fillna(0)
        occupancyAxes.plot(dailyOccupancy, label = str(day), marker = "o", markersize = 6, linewidth = 3, color = colors[n])
        # Average Occupancy Rate between 8AM and 8PM
        occAvg.append(dailyOccupancy.ix[8:20].mean())
        n+=1
        
    
    occupancyAxes.axhline(np.mean(occAvg), color='black', linewidth=2)
    occupancyAxes.legend()
    
    # Plot Occupancy Box Plots
    sns.set_style("whitegrid")
    
    grey = ["#64686d", "#64686d", "#64686d", "#64686d", "#64686d", "#64686d"]
    sns.set_palette(grey)
    
    occBoxFig = plt.figure(figsize = (18,10))
    occBoxAxes = occBoxFig.add_axes([0,0,1,1])
    occBoxAxes.set_ylim([0,1.2])
    
    # Just Occupancy Rate between 8AM and 8PM
    sns.boxplot(data = holder[(holder["Hour"] >= 8) & 
                              (holder["Hour"] <= 20)][["Class Hours Percentage", "Day of Week", "Hour"]].dropna(), 
                y = "Class Hours Percentage",
                x = "Day of Week",
                width = .5
               )
    occBoxAxes.set_title("Average Occupancy Rate by Day")
    occBoxAxes.set_ylabel("Average Occupancy %")
    
    # Plot Utilization by Day and Hour
    plt.style.use("seaborn-whitegrid")
    utilizationFigure = plt.figure(figsize = (18,10))
    utilizationAxes = utilizationFigure.add_axes([0,0,1,1])
    utilizationAxes.set_title("Average Utilizaion Rate by Date", fontsize = 20)
    utilizationAxes.set_xlabel("Time of Day")
    utilizationAxes.set_ylabel("Average Utilization %")
    utilizationAxes.set_ylim([0,1.2])
    utilizationAxes.set_xlim([0,23])
    plt.xticks(np.arange(0,24, 1.0))
    
    utilAvg = []
    n = 0
    for day in holder["Day of Week"].unique().tolist():
        dailyUtilization = holder[holder["Day of Week"] == day][["Hour", "Class capacity", "Class Enrollment"]].copy()
        dailyUtilization.dropna(inplace = True)
        dailyUtilization["Utilization"] = dailyUtilization["Class Enrollment"] / dailyUtilization["Class capacity"]
        dailyUtilization = dailyUtilization.groupby("Hour")["Utilization"].mean()
        dailyUtilization = pd.DataFrame(dailyUtilization, index = np.arange(0,24).tolist()).fillna(0)
        utilizationAxes.plot(dailyUtilization, label = str(day), marker = "o", markersize = 6, linewidth = 3, color = colors[n])
        utilAvg.append(dailyUtilization["Utilization"].ix[8:20].mean())
        n+=1
    
    utilizationAxes.axhline(np.mean(utilAvg), color='black', linewidth=2)
    utilizationAxes.legend()
    
    # Utilization Box Plot
    sns.set_style("whitegrid")
    sns.set_palette(grey)
    
    utilBoxFig = plt.figure(figsize = (18,10))
    utilBoxAxes = utilBoxFig.add_axes([0,0,1,1])
    utilBoxAxes.set_ylim([0,1.2])
    
    holder["Utilization"] = holder["Class Enrollment"] / holder["Class capacity"]
    sns.boxplot(data =  holder[(holder["Hour"] >= 8) & 
                              (holder["Hour"] <= 20)][["Day of Week", "Utilization"]].dropna(),
               y = "Utilization",
               x = "Day of Week",
               width = .5
               )
    utilBoxAxes.set_title("Average Utilization Rate by Day")
    utilBoxAxes.set_ylabel("Average Utilization %")
    