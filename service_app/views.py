from django.shortcuts import render
from common_app.models import State, City
from iran_cities import iran_cities_list

from django.views.generic import TemplateView

# Create your views here.

class Home_view(TemplateView):
    template_name = 'service_app/home.html' 
    
    if State.objects.count() == 0:
        for i,j in enumerate(iran_cities_list):

            state_object = State.objects.create(title=j.get('province'))
            cities = j.get('cities')
            for city in cities:
                City.objects.create(state=state_object , title=city)


