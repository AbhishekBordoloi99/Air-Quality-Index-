import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_data2013():
    temp_i=0
    average=[]
    for rows in pd.read_csv("Data/AQI/aqi2013.csv", chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="InVld":
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
    return average
def extract_data2014():
    temp_i=0
    average=[]
    for rows in pd.read_csv("Data/AQI/aqi2014.csv", chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="InVld":
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
    return average

def extract_data2015():
    temp_i=0
    average=[]
    for rows in pd.read_csv("Data/AQI/aqi2015.csv", chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="InVld" and i!="---":
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
    return average

def extract_data2016():
    temp_i=0
    average=[]
    for rows in pd.read_csv("Data/AQI/aqi2016.csv", chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="InVld":
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
    return average

def extract_data2017():
    temp_i=0
    average=[]
    for rows in pd.read_csv("Data/AQI/aqi2017.csv", chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="InVld":
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
    return average

def extract_data2018():
    temp_i=0
    average=[]
    for rows in pd.read_csv("Data/AQI/aqi2018.csv", chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="InVld":
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        average.append(avg)
    return average


if __name__=="__main__":
    data_2013=extract_data2013()
    data_2014=extract_data2014()
    data_2015=extract_data2015()
    data_2016=extract_data2016()
    data_2017=extract_data2017()
    data_2018=extract_data2018()
    plt.plot(range(0,365), data_2013, color='blue')
    plt.plot(range(0,365), data_2015, color='red')