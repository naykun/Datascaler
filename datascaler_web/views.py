from django.shortcuts import render
from datascaler_web.models import *
import json
# Create your views here.
def index(request):
    return render(request,"index.html")

def chart(request):
    return render(request,"chart.html")
def doc(request):
    return render(request,"doc.html")
def air(request):
    air_date=request.GET.get("time")
    sta_id=int(request.GET.get("station"))
    try :
        item=airquality.objects(time=air_date,station_id=sta_id)[0]
        info=json.loads(item.to_json())
        sta=station.objects(station_id=sta_id)
        info2 = json.loads(sta.to_json())
        info['latitude']=info2[0]['latitude']
        info['longitude']=info2[0]['longitude']
    except:
        info={"error":"nosuchinfo"}
    return render(request,"xxx.html",info)