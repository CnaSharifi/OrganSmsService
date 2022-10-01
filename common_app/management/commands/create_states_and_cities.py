
from common_app.models import State, City
from django.core.management.base import BaseCommand
from iran_cities import iran_cities_list

import random
import time

class Command(BaseCommand):
    help = 'Create states and cities'

    def add_arguments(self, parser):
        pass
    
    def handle(self, *args, **kwargs):
        if State.objects.count() == 0:
            for i,j in enumerate(iran_cities_list):

                state_object = State.objects.create(title=j.get('province'))
                cities = j.get('cities')
                for city in cities:
                    City.objects.create(state=state_object , title=city)