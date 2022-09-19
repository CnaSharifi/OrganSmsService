from django.db import models

# Create your models here.
class State(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
