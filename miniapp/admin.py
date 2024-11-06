from django.contrib import admin
from .models import *

models = [CustomUser, AuditFile, BinSaver]

# Register your models here.
admin.site.register(models)
