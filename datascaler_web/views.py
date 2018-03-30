from django.shortcuts import render
from datascaler_web.models import *
from django.http import JsonResponse
import json
import re
from datetime import datetime, timedelta
# Create your views here.
def index(request):
    return render(request,"index.html")
def chart(request):
    return render(request,"chart.html")
def doc(request):
    return render(request,"doc.html")
def process(month):
    if month=="Jan":
        return '1'
    if month=="Feb":
        return '2'
    if month=="Mar":
        return '3'
    if month=='Apr':
        return '4'
    if month=='May':
        return '5'
    if month=='Jun':
        return '6'
    if month=='Jul':
        return '7'
    if month=='Aug':
        return '8'
    if month=='Sep':
        return '9'
    if month=='Oct':
        return '10'
    if month=='Nov':
        return '11'
    if month=='Dec':
        return '12'
#def air_12h(request):
#    air_date = request.GET.get("time").split(' ')
#    air_date = air_date[3] + ' ' + process(air_date[1]) + " " + air_date[2] + " " + air_date[4]
#    return air_12h_id_date()

def air(request):
    print("SOME")
    air_date=request.GET.get("time").split(' ')
    air_date=air_date[3]+' '+process(air_date[1])+" "+air_date[2]+" "+air_date[4]
    print(air_date)


    try:
        id=request.GET.get("station_id")
        print(str(id)+"<----id")
        if(id!=None):
            print ("CASE1")
            return air_12h_id_date(id,air_date)

    except:
        pass

    print("CASE2")

    try :
        items=airquality.objects(time=air_date)
        return_items={}
        for i,item in enumerate(items):
            info=json.loads(item.to_json())
            sta=station.objects(station_id=info['station_id'])[0]
            info2 = json.loads(sta.to_json())
            info['latitude']=info2['latitude']
            info['longitude']=info2['longitude']
            info['name_chinese']=info2['name_chinese']
            return_items[i]=info
    except:
        info={"error":"nosuchinfo"}
        print("an error //oops\n\n\n\n\n\n\n\n\n\n\n ")
    return JsonResponse(return_items)

def air_12h_id_date(id,date):
    timenow=datetime.strptime(date,"%Y %m %d %H:%M:%S")
    air_all_time={}
    for i in range(-6,7):
        new_time=timenow+timedelta(hours=i)
        new_time_str=str(new_time)

        try:
            all_items=airquality.objects(time=new_time_str,station_id=id)
            #should only be one item ,not items
        except:
            all_items=[]
        return_items = {}
        try:
            item=all_items[0]
            info = json.loads(item.to_json())
            sta = station.objects(station_id=info['station_id'])[0]
            info2 = json.loads(sta.to_json())
            info['latitude'] = info2['latitude']
            info['longitude'] = info2['longitude']
            info['name_chinese'] = info2['name_chinese']
            return_items= info
            air_all_time[i]=return_items
        except:
            air_all_time[i]={}

    #return air_all_time
    return JsonResponse(air_all_time)









