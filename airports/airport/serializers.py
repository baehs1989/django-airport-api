from rest_framework import serializers
from . import models

class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Airport
        fields = ('airport_id', 'name', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'altitude',
                  'timezone', 'dst', 'tz', 'type', 'source')
        extra_kwargs = {"airport_id": {'read_only': True}}

