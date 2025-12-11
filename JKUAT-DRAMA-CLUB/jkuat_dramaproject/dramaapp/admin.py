from django.contrib import admin
from .import models # models

# Register your models here.

admin.site.register(models.Member) # register member model
admin.site.register(models.Event) # register event model
