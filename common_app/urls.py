# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import CityAPIView, StateViewSet

router = routers.DefaultRouter()
router.register(r'states', StateViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('cities/<int:stateID>/', CityAPIView.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]