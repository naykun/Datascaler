from django.shortcuts import render
from datascaler_web.models import *
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
    print(request.GET)
    #pat=re.compile(r'\d{4}.*\d{2}\:\d{2}\:\d{2}')
    air_date=request.GET.get("time").split(' ')
    air_date=air_date[3]+' '+process(air_date[1])+" "+air_date[2]+" "+air_date[4]
    #air_date=pat.findall(air_date)[0]
    sta_id=int(request.GET.get("station_id"))
    print(air_date)
    print(sta_id)
    try :
        item=airquality.objects(time=air_date,station_id=sta_id)[0]
        info=json.loads(item.to_json())
        sta=station.objects(station_id=sta_id)[0]
        info2 = json.loads(sta.to_json())
        #print(info2)
        #print(info)
        info['latitude']=info2['latitude']
        info['longitude']=info2['longitude']
    except:
        info={"error":"nosuchinfo"}
        print("an error //oops\n\n\n\n\n\n\n\n\n\n\n ")
    return render(request,"chart.html",info)
