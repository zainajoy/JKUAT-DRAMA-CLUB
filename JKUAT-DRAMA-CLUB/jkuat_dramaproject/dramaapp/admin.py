from django.contrib import admin
from .import models # models

# Register your models here.

admin.site.register(models.member) # register member model
admin.site.register(models.event) # register event model
admin.site.register(models.gallery) # register gallery  model
