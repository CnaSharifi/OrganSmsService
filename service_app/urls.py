# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import ServiceViewSet
from .views import Home_view

from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'messages', ServiceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('app/',login_required(Home_view.as_view())),

    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]