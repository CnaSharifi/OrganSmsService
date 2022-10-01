from rest_framework import viewsets

from .serializers import CitySerializer, StateSerializer
from .models import State, City

# Create your views here.

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all().order_by('id')
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_queryset(self): 
        parent = self.request.query_params.get('parent',None)
        #regions = self.request.query_params.get("regions", None)
        if parent:
            qs = City.objects.filter(state=parent)
            pass
        else:
            qs = City.objects.all()
        return qs
