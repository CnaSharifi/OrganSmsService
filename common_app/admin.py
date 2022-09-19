from django.contrib import admin

from .models import State, City
# Register your models here.

class StateModelAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    ordering = ['id']

class CityModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','state']
    ordering = ['id']
    search_fields = ['title']

admin.site.register(State,StateModelAdmin)
admin.site.register(City,CityModelAdmin)
