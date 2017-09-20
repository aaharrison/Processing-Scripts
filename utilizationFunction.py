# Be sure to pip install the following python libraries (https://www.youtube.com/watch?v=jnpC_Ib_lbc)
import os
import numpy as np
import pandas as pd
import datetime
from datetime import date, timedelta


 # Utilization Function Initiated
def utilization(test, start = "dt_start", end = "dt_end"):

    try:
        holder["dt_start"] = holder["dt_start"].apply(lambda x: datetime.datetime.strptime(x, "%m/%d/%y %H:%S"))
        holder["dt_end"] = holder["dt_end"].apply(lambda x: datetime.datetime.strptime(x, "%m/%d/%y %H:%S"))
    except:
        pass

    test["zero"] = 0
    test["one"] = 0
    test["two"] = 0
    test["three"] = 0
    test["four"] = 0
    test["five"] = 0
    test["six"] = 0
    test["seven"] = 0
    test["eight"] = 0
    test["nine"] = 0
    test["ten"] = 0
    test["eleven"] = 0 
    test["twelve"] = 0
    test["thirteen"] = 0
    test["fourteen"] = 0
    test["fifteen"] = 0
    test["sixteen"] = 0
    test["seventeen"] = 0
    test["eighteen"] = 0
    test["nineteen"] = 0
    test["twenty"] = 0
    test["twenty one"] = 0
    test["twenty two"] = 0 
    test["twenty three"] = 0

    translate = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three"
    }


    n = 0
    for start, end in zip(test[start], test[end]):
        for hour in np.arange(0,24):
            if start.hour == hour and end.hour == hour:
                holder = (60 - start.minute)
                holder2 = (end.minute)
                test.iloc[n, test.columns.get_loc(translate[hour])] = holder + holder2
            elif start.hour == hour and end.hour == hour + 1:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = end.minute
            elif start.hour == hour and end.hour == hour + 2:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = end.minute
            elif start.hour == hour and end.hour == hour + 3:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = end.minute
            elif start.hour == hour and end.hour == hour + 4:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = end.minute
            elif start.hour == hour and end.hour == hour + 5:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 5])] = end.minute
            elif start.hour == hour and end.hour == hour + 6:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 5])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 6])] = end.minute
            elif start.hour == hour and end.hour == hour + 7:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 5])] = 60                
                test.iloc[n, test.columns.get_loc(translate[hour + 6])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 7])] = end.minute
            elif start.hour == hour and end.hour == hour + 8:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 5])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 6])] = 60                
                test.iloc[n, test.columns.get_loc(translate[hour + 7])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 8])] = end.minute
            elif start.hour == hour and end.hour == hour + 9:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 5])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 6])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 7])] = 60                
                test.iloc[n, test.columns.get_loc(translate[hour + 8])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 9])] = end.minute
            elif start.hour == hour and end.hour == hour + 10:        
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 5])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 6])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 7])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 8])] = 60                
                test.iloc[n, test.columns.get_loc(translate[hour + 9])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 10])] = end.minute
            elif start.hour == hour and end.hour == hour + 11:
                test.iloc[n, test.columns.get_loc(translate[hour])] = 60 - start.minute
                test.iloc[n, test.columns.get_loc(translate[hour + 1])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 2])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 3])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 4])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 5])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 6])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 7])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 8])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 9])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 10])] = 60
                test.iloc[n, test.columns.get_loc(translate[hour + 11])] = end.minute                
            else:
                pass
        n+=1


    test.to_csv("Utilization Data Output.csv", index = False)

# Edit Perameters for Function Below

# Below in the 'os.chdir' function paste in the directory location for the file you are looking to transform
os.chdir("/Users/adeniyiharrison/Desktop")

# Currently where 'stanford-class-data.xlsx' is replace with the name of the file you would like to transform
# sheetname parameter should equal the name of the tab in the excel file that has the data that needs to be transformed
# If you are using a csv and not an excel file remove the read excel line and uncomment the line with read csv 

holder = pd.read_excel("stanford-class-data.xlsx", sheetname = "class")


# holder = pd.read_csv("stanford-class-data.csv")

# Update the start and end parameters with the column names of the respective start date/time and end date/time
# Ensure that the start and end date/time columns are actually date/time data types and not string formats (only datetime will work) 
utilization(holder, start = "dt_start", end = "dt_end")



