from django.db import models

from common_app.models import City
# Create your models here.
class ServiceModel(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    content = models.TextField(null=False,blank=False)

    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
