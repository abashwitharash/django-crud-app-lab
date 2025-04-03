from django.contrib import admin

# Register your models here.
from .models import Shoe, Cleaning

admin.site.register(Shoe)
admin.site.register(Cleaning)