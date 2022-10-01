from django.shortcuts import render
from common_app.models import State, City
from iran_cities import iran_cities_list
from django.views.generic import TemplateView

from .serializers import ServiceSerializer
from .models import ServiceModel
from rest_framework import viewsets

# Create your views here.

class Home_view(TemplateView):
    template_name = 'service_app/home.html' 



class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all().order_by('timestamp')
    serializer_class = ServiceSerializer    


