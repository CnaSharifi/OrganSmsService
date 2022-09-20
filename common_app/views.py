from rest_framework import viewsets
from rest_framework import generics

from .serializers import CitySerializer, StateSerializer
from .models import State, City

# Create your views here.

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all().order_by('id')
    serializer_class = StateSerializer



class CitiesOfStateAPIView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        stateID = self.kwargs['stateID']
        qs = City.objects.filter(state=stateID)
        return  qs.order_by('id')

class CityAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
