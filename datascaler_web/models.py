from django.db import models
from mongoengine import *
# Create your models here.

class DataInfo(Document):
    des = StringField()
