#!/usr/bin/env python
"""
load .csv file 
airquality.csv  district.csv      weatherforecast.csv
city.csv      meteorology.csv    station.csv

Usage:
util.py path_to_data

数据很大 很慢 大概一个多小时吧
"""
['004', '深圳', 'ShenZhen', '22.543099', '114.057868', '2']
import csv
import sys
import os
from mongoengine import *
from models import *
connect('datascaler')
def load_city_item(city_item):
    """
    input should be like this 
    [4, '深圳', 'ShenZhen', 22.543099, 114.057868, 2]
    """
    city(*city_item).save()
    #city(city_id=int(city_item[0]),name_chinese=city_item[1],name_english=city_item[2],latitude=float(city_item[3]),longitude=float(city_item[4]),cluster_id=int(city_item[5]).save()
def load_dist_item(dist_item):
    district(*dist_item).save()
def load_weat_item(weat_item):
    weatherforecast(*weat_item).save()
def load_airq_item(airq_item):
    airquality(*airq_item).save()
def load_mete_item(mete_item):
    meteorology(*mete_item).save()
def load_stat_item(stat_item):
    station(*stat_item).save()
    
def init_load(path):
    os.chdir(path)
    file=csv.reader(open("meteorology.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        #print(item)
        load_mete_item(item)
    print("ok")
    file=csv.reader(open("weatherforecast.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        load_weat_item(item)
    print("ok")
    file=csv.reader(open("city.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        load_city_item(item)
    print("ok")
    file=csv.reader(open("district.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        load_dist_item(item)
    print("ok")
    file=csv.reader(open("station.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        load_stat_item(item)
    print("ok")
    file=csv.reader(open("airquality.csv","r"))
    next(file)
    for item in file:
        item=[None if i=="NULL" else i for i in item]
        load_airq_item(item)

def main(path):
    init_load(path)
    
if __name__=="__main__":
    print(sys.argv)
    main(sys.argv[1])
     
                   
    
    
    
    