from django.contrib import admin
from .models import *
from django.contrib.admin import site

# Register your models here.
admin.site.register(Task)