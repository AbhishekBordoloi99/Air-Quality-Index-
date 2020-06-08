from AQI_data import extract_data2013,extract_data2014,extract_data2015,extract_data2016,extract_data2017,extract_data2018
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup 
import csv
import os

def scrap_data(month,year):
    
    temp=[]
    final=[]
    file_html=open("Data\Html_data\{}\{}.html".format(year,month),"rb").read()
    soup=BeautifulSoup(file_html, "lxml") 
    
    for table in soup.find_all("table",{"class":"medias mensuales numspan"}):
        for tbody in table:
            for tr in tbody:
                a=tr.get_text()
                temp.append(a)
     
    rows=len(temp)/15
    
    for times in range(round(rows)):
        newtemp=[]
        for i in range(15):
            newtemp.append(temp[0])
            temp.pop(0)
        
        final.append(newtemp)

    length = len(final)

    final.pop(length - 1)
    final.pop(0)

    for a in range(len(final)):
        final[a].pop(6)
        final[a].pop(13)
        final[a].pop(12)
        final[a].pop(11)
        final[a].pop(10)
        final[a].pop(9)
        final[a].pop(0)

    return final


def data_combine(year,cs):
    for a in pd.read_csv('Data/Real-Data/data_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
        print(df)
    return mylist
    
    
    
if __name__=="__main__":
    
    if not os.path.exists("Data\Real-data"):
        os.makedirs("Data\Real-data")
    for year in range(2013,2017):
        final_data=[]
        with open("Data\Real-data\data_{}.csv".format(year), "w") as csvfile:
            wr=csv.writer(csvfile,dialect="excel")
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
    
        for month in range(1,13):
            temp=scrap_data(month,year)
            final_data=final_data+temp
            
    
        pm= getattr(sys.modules[__name__], 'extract_data{}'.format(year))()
        
        for i in range(len(final_data)-1):
            final_data[i].insert(8, pm[i])
            
        with open("Data\Real-data\data_{}.csv".format(year), "a") as csvfile:
            wr=csv.writer(csvfile, dialect="excel")
            
            for row in final_data:
                flag=0
                for elem in row:
                    if elem=="" and elem=="-":
                        flag=1
                
                if flag!=1:
                    wr.writerow(row)
                
            
            
    data_2013 = data_combine(2013, 200)
    data_2014 = data_combine(2014, 200)
    data_2015 = data_combine(2015, 200)
    data_2016 = data_combine(2016, 200)
     
    total=data_2013+data_2014+data_2015+data_2016
    
    with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm','SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
            
            
            
            
df=pd.read_csv("Data/Real-data/Real_Combine.csv")
df=df.dropna()
df=df.drop(columns=['SLP'], axis=1)
            
            
            
            
    
    
    
    