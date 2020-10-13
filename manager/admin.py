from django.contrib import admin

from django.contrib import admin

# Register your models here.

from .models import Manager, Tourist  # ,Project

admin.site.register([Manager, Tourist])
# admin.site.register(Project)
