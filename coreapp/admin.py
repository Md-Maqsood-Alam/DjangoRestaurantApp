from django.contrib import admin
from .models import Dish, Reservation
# Register your models here.
admin.site.register(Dish)
admin.site.register(Reservation)