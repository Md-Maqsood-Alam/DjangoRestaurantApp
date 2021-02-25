from django.shortcuts import render
from .models import Dish
# Create your views here.
def home(request):
    menu=dict()
    menu['Starters']=Dish.objects.filter(dish_type='Starters')|Dish.objects.filter(dish_type='Momos')|Dish.objects.filter(dish_type='Soups')
    menu['Main_Dishes']=Dish.objects.filter(dish_type='Main Course')|Dish.objects.filter(dish_type='Bread')|Dish.objects.filter(dish_type='Others')
    menu['Noodles_and_Rice']=Dish.objects.filter(dish_type='Fried Rice and Noodles')
    menu['Rolls']=Dish.objects.filter(dish_type='Rolls')
    return render(request,'index.html',{'menu':menu})

def reservation(request):
    return render(request,'reservation.html')