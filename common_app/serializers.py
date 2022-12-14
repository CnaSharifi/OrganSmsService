from rest_framework import serializers

from .models import State, City

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'title')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        
