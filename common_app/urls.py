# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import CityAPIView,CitiesOfStateAPIView,  StateViewSet

router = routers.DefaultRouter()
router.register(r'state', StateViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('city/<int:stateID>/', CitiesOfStateAPIView.as_view()),
    path('city/', CityAPIView.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]