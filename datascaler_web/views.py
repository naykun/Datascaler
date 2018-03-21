from django.shortcuts import render
from datascaler_web.models import *
from django.http import JsonResponse
import json
import re
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
def air(request):
    air_date=request.GET.get("time").split(' ')
    air_date=air_date[3]+' '+process(air_date[1])+" "+air_date[2]+" "+air_date[4]
    try :
        items=airquality.objects(time=air_date)
        return_items={}
        for i,item in enumerate(items):
            info=json.loads(item.to_json())
            if (item['station_id']>=1001 and item['station_id']<=1036) or(item['station_id']>=6001 and item['station_id']<=6028):
                sta=station.objects(station_id=info['station_id'])[0]
                info2 = json.loads(sta.to_json())
                info['latitude']=info2['latitude']
                info['longitude']=info2['longitude']
                info['name_chinese']=info2['name_chinese']
                return_items[i]=info
    except:
        info={"error":"nosuchinfo"}
        print("an error //oops\n\n\n\n\n\n\n\n\n\n\n ")
    return JsonResponse(info)
