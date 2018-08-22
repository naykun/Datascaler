from mongoengine import *
# Create your models here.

class DataInfo(Document):
    des = StringField(null=True)
class city(Document):
    city_id=IntField(null=True)
    name_chinese=StringField(null=True)
    name_english=StringField(null=True)
    latitude=FloatField(null=True)
    longitude=FloatField(null=True)
    cluster_id=IntField(null=True)
class airquality(Document):
    station_id=IntField(null=True)
    time=DateTimeField(null=True)
    PM25_Concentration=IntField(null=True)
    PM10_Concentration=FloatField(null=True)
    NO2_Concentration=FloatField(null=True)
    CO_Concentration=FloatField(null=True)
    O3_Concentration=FloatField(null=True)
    SO2_Concentration=FloatField(null=True)
class district(Document):
    district_id=IntField(null=True)
    name_chinese=StringField(null=True)
    ame_english=StringField(null=True)
    city_id=IntField(null=True)
class meteorology(Document):
    idx=IntField(null=True)
    time=DateTimeField(null=True)
    weather=IntField(null=True)
    temperature=FloatField(null=True)
    pressure=FloatField(null=True)
    humidity=FloatField(null=True)
    wind_speed=FloatField(null=True)
    wind_direction=IntField(null=True)
class station(Document):
    station_id=IntField(null=True)
    name_chinese=StringField(null=True)
    name_english=StringField(null=True)
    latitude=FloatField(null=True)
    longitude=FloatField(null=True)
    district_id=IntField(null=True)
class weatherforecast(Document):
    idx=IntField(null=True)
    time_forecast=DateTimeField(null=True)
    time_future=DateTimeField(null=True)
    frequent=IntField(null=True)
    weather=IntField(null=True)
    up_temperature=FloatField(null=True)
    bottom_temperature=FloatField(null=True)
    wind_level=FloatField(null=True)
    wind_direction=IntField(null=True)
class image(Document):
    station_id=IntField(null=True)
    image=FileField(null=True)

    

    