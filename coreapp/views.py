from django.shortcuts import render, redirect
from .models import Dish, Reservation
from django.urls import reverse
from datetime import datetime
from django.contrib import messages
# Create your views here.
def home(request):
    menu=dict()
    menu['Starters']=Dish.objects.filter(dish_type='Starters')|Dish.objects.filter(dish_type='Momos')|Dish.objects.filter(dish_type='Soups')
    menu['Main_Dishes']=Dish.objects.filter(dish_type='Main Course')|Dish.objects.filter(dish_type='Bread')|Dish.objects.filter(dish_type='Others')
    menu['Noodles_and_Rice']=Dish.objects.filter(dish_type='Fried Rice and Noodles')
    menu['Rolls']=Dish.objects.filter(dish_type='Rolls')
    return render(request,'index.html',{'menu':menu})

def reservation(request):
    if request.method=='POST':
        reservation=Reservation(
            name=request.POST.get('form_name'),
            email=request.POST.get('email'),
            phone_number=(request.POST.get('phone')),
            num_people=request.POST.get('no_of_persons'),
            date_and_time=datetime.strptime('{} {}'.format(
                request.POST.get('date-picker'),
                request.POST.get('time-picker')
            ), '%d.%m.%Y %H:%M %p'),
            )
        reservation.save()
        if request.user.is_authenticated:
            request.user.reservation_set.add(reservation)
        messages.add_message(request,messages.INFO, 'Your Reservation Has been Made Successfully')
        return redirect(reverse('home'))
    return render(request,'reservation.html')