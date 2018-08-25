from django.db import models
import os

class Airport(models.Model):
    airport_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    iata = models.CharField(max_length=100)
    icao = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    timezone = models.FloatField()
    dst = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    source = models.CharField(max_length=100)

    # def __init__(self, airport_id, name, city, country, iata, icao, latitude, longitude, altitude, timezone, dst, tz, type, source):
    #     self.airport_id = airport_id
    #     self.name = name
    #     self.city = city
    #     self.country = country
    #     self.iata = iata
    #     self.icao = icao
    #     self.latitude = latitude
    #     self.longitude = longitude
    #     self.altitude = altitude
    #     self.timezone = timezone
    #     self.dst = dst
    #     self.tz = tz
    #     self.type = type
    #     self.source = source

    def __str__(self):
        return str(self.name)

    def update(self, **kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')
        self.country = kwargs.get('country')
        self.iata = kwargs.get('iata')
        self.icao = kwargs.get('icao')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.altitude = kwargs.get('altitude')
        self.timezone = kwargs.get('timezone')
        self.dst = kwargs.get('dst')
        self.tz = kwargs.get('tz')
        self.type = kwargs.get('type')
        self.source = kwargs.get('source')

    @staticmethod
    def format():
        return {'airport_id':0, 'name':1, 'city': 2, 'country': 3, 'iata':4,
                'icao':5, 'latitude':6, 'longitude':7, 'altitude':8, 'timezone':9,
                'dst':10, 'tz':11, 'type':12, 'source:':13}

    class Meta():
        ordering = ['airport_id']