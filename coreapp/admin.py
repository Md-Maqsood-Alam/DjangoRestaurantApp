from django.contrib import admin
from .models import Dish, Reservation, Order, TodaysSpecials
# Register your models here.
admin.site.register(Dish)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(TodaysSpecials)