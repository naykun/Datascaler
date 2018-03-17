from django.shortcuts import render
from models import *
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
    sta_id=request.GET.get("station")
    try :
        item=airquality.objects(time=air_date,station_id=sta_id)[0]
        info=json.loads(item.to_json())
    except:
        info={"error":"nosuchinfo"}
    return render(request,"xxx.html",info)