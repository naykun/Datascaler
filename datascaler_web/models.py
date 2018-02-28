from django.db import models
from mongoengine import *
# Create your models here.

class DataInfo(Document):
    des = StringField()
    
class city(models.Model):
    city_id=models.IntegerField(default= 0)
    name_chinese=models.CharField(max_length=20)
    name_english=models.CharField(max_length=20)
    latitude=models.DecimalField(max_digits=20, decimal_places=8)
    longitude=models.DecimalField(max_digits=20, decimal_places=8)
    cluster_id=models.IntegerField(default= 0)
class airq(models.Model):
    station_id=models.IntegerField(default= 0)
    time=models.DateTimeField(auto_now_add=True)
    PM25_Concentration=models.IntegerField(default= 0)
    PM10_Concentration=models.DecimalField(max_digits=5, decimal_places=3)
    NO2_Concentration=models.DecimalField(max_digits=5, decimal_places=3)
    CO_Concentration=models.DecimalField(max_digits=5, decimal_places=3)
    O3_Concentration=models.DecimalField(max_digits=5, decimal_places=3)
    SO2_Concentration=models.DecimalField(max_digits=5, decimal_places=3)
class district(models.Model):
    district_id=models.IntegerField(default= 0)
    name_chinese=models.CharField(max_length=20)
    ame_english=models.CharField(max_length=20)
    city_id=models.IntegerField(default= 0)
class meteorology(models.Model):
    idx=models.IntegerField(default= 0)
    time=models.DateTimeField(auto_now_add=True)
    weather=models.IntegerField(default= 0)
    temperature=models.DecimalField(max_digits=5, decimal_places=3)
    pressure=models.DecimalField(max_digits=5, decimal_places=3)
    humidity=models.IntegerField(default= 0)
    wind_speed=models.DecimalField(max_digits=5, decimal_places=3)
    wind_direction=models.IntegerField(default= 0)
class station(models.Model):
    station_id=models.IntegerField(default= 0)
    name_chinese=models.CharField(max_length=20)
    name_english=models.CharField(max_length=20)
    latitude=models.DecimalField(max_digits=20, decimal_places=8)
    longitude=models.DecimalField(max_digits=20, decimal_places=8)
    district_id=models.IntegerField(default= 0)
class weatherforecast(models.Model):
    idx=models.IntegerField(default= 0)
    time_forecast=models.DateTimeField(auto_now_add=True)
    time_future=models.DateTimeField(auto_now_add=True)
    frequent=models.IntegerField(default= 0)
    weather=models.IntegerField(default= 0)
    up_temperature=models.IntegerField(default= 0)
    bottom_temperature=models.IntegerField(default= 0)
    wind_level=models.IntegerField(default= 0)
    wind_direction=models.IntegerField(default= 0)


    

    