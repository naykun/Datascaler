#!/usr/bin/env python
"""
load .csv file 
airquality.csv  district.csv      weatherforecast.csv
city.csv      meteorology.csv    station.csv

Usage:
util.py path_to_data
数据很大 很慢 大概20分钟
"""
['004', '深圳', 'ShenZhen', '22.543099', '114.057868', '2']
import csv
import sys
import os
from mongoengine import *
from models import *
connect('datascaler')
def load_city_item(city_item,save=False):
    """
    input should be like this 
    [4, '深圳', 'ShenZhen', 22.543099, 114.057868, 2]
    """
    if save :
        city(*city_item).save()
    else:
        return city(*city_item)
    #city(city_id=int(city_item[0]),name_chinese=city_item[1],name_english=city_item[2],latitude=float(city_item[3]),longitude=float(city_item[4]),cluster_id=int(city_item[5]).save()
def load_dist_item(dist_item,save=False):
    if save:
        district(*dsit_item).save()
    else:
        return district(*dist_item)
def load_weat_item(weat_item,save=False):
    if save:
        weatherforecast(*weat_item).save()
    else:
        return weatherforecast(*weat_item)
def load_airq_item(airq_item,save=False):
    if save:
        airquality(*airq_item).save()
    else:
        return airquality(*airq_item)
def load_mete_item(mete_item,save=False):
    if save:
        meteorology(*mete_item).save()
    else:
        return meteorology(*mete_item)
def load_stat_item(stat_item,save=False):
    if save:
        station(*stat_item).save()
    else:
        return station(*stat_item)
def init_load(path):
    os.chdir(path)
    list_data=[]
    file = csv.reader(open("city.csv", "r"))
    next(file)
    for item in file:
        item = [None if i == "NULL" else i for i in item]
        list_data.append(load_city_item(item))
    city.objects.insert(list_data)
    print("ok")

    list_data = []
    file = csv.reader(open("weatherforecast.csv", "r"))
    next(file)
    for item in file:
        item = [None if i == "NULL" else i for i in item]
        list_data.append(load_weat_item(item))
    weatherforecast.objects.insert(list_data, load_bulk=False)
    print("ok")

    list_data=[]
    file=csv.reader(open("meteorology.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        #print(item)
        list_data.append(load_mete_item(item))
    meteorology.objects.insert(list_data,load_bulk=False)
    print("ok")

    list_data=[]
    file=csv.reader(open("district.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        list_data.append(load_dist_item(item))
    district.objects.insert(list_data)
    print("ok")

    list_data=[]
    file=csv.reader(open("station.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        list_data.append(load_stat_item(item))
    station.objects.insert(list_data)
    print("ok")

    list_data=[]
    file=csv.reader(open("airquality.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        list_data.append(load_airq_item(item))
    airquality.objects.insert(list_data,load_bulk=False)
    print("work done")

def main(path):
    init_load(path)
    
if __name__=="__main__":
    main(sys.argv[1])
     
                   
    
    
    
    