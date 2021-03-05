from django.shortcuts import render, redirect
from .models import Dish, Reservation, Order, TodaysSpecials
from django.urls import reverse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from foodcart.views import cart_clear_silent
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    menu=dict()
    menu['Starters']=Dish.objects.filter(dish_type='Starters')|Dish.objects.filter(dish_type='Momos')|Dish.objects.filter(dish_type='Soups')
    menu['Main_Dishes']=Dish.objects.filter(dish_type='Main Course')|Dish.objects.filter(dish_type='Bread')|Dish.objects.filter(dish_type='Others')
    menu['Noodles_and_Rice']=Dish.objects.filter(dish_type='Fried Rice and Noodles')
    menu['Rolls']=Dish.objects.filter(dish_type='Rolls')
    todaysSpecials=TodaysSpecials.objects.last().dishes.all()
    return render(request,'index.html',{'menu':menu, 'todaysSpecials': todaysSpecials})

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
        if request.POST.get('occasion'):
            reservation.occasion=request.POST.get('occasion')
        reservation.save()
        if request.user.is_authenticated:
            request.user.reservation_set.add(reservation)
        messages.add_message(request,messages.INFO, 'Your Reservation Has been Made Successfully')
        return redirect(reverse('home'))
    return render(request,'reservation.html')

@login_required
def order(request):
    if 'cart' not in request.session:
        return redirect(reverse('home'))
    menu=dict()
    menu['Starters']=list(Dish.objects.filter(dish_type='Starters')|Dish.objects.filter(dish_type='Momos')|Dish.objects.filter(dish_type='Soups'))
    menu['Main_Dishes']=list(Dish.objects.filter(dish_type='Main Course')|Dish.objects.filter(dish_type='Bread')|Dish.objects.filter(dish_type='Others'))
    menu['Noodles_and_Rice']=list(Dish.objects.filter(dish_type='Fried Rice and Noodles'))
    menu['Rolls']=list(Dish.objects.filter(dish_type='Rolls'))
    subtotal=sum((int(request.session['cart'][i]['price'])*int(request.session['cart'][i]['quantity']) for i in request.session['cart']))
    if 'q' in request.GET:
        for dishType in menu:
            menu[dishType]=list(filter(lambda x: (request.GET['q'].lower() in x.name.lower()) or (request.GET['q'].lower() in x.description.lower()), menu[dishType]))
        return render(request, 'order.html', {'menu': menu, 'subtotal': subtotal, 'searched_for': request.GET['q']})
    else:
        return render(request, 'order.html', {'menu':menu, 'subtotal': subtotal})
    
@login_required
def checkout(request):
    if 'cart' not in request.session:
        return redirect(reverse('home'))
    subtotal=sum((int(request.session['cart'][i]['price'])*int(request.session['cart'][i]['quantity']) for i in request.session['cart']))
    delivery_charge = 20 if subtotal<300 else 0
    to_pay = subtotal+delivery_charge  
    try:
        currentCustomer=request.user.customer
    except ObjectDoesNotExist:
        messages.add_message(request,messages.INFO,"Please complete your profile to place an order.")
        return redirect(reverse('profile_create'))    
    if request.method=='POST':
        try:
            dishesOrdered={ request.session['cart'][i]['product_id']:(request.session['cart'][i]['name'],request.session['cart'][i]['quantity']) for i in request.session['cart'] }
            order=Order(
                date_and_time=datetime.now(),
                customer=currentCustomer,
                dishes_ordered=repr(dishesOrdered),
                dishes_total=subtotal,
                delivery_charge=delivery_charge,
                delivery_address=request.POST.get('delivery_address'),
                )
            order.save()
            messages.add_message(request, messages.INFO, 'Order placed Successfully. Your Food is on it\'s way!')
            cart_clear_silent(request)
            return redirect(reverse('home'))
        except:
            messages.add_message(request, messages.INFO, "Something went wrong! Please order by call or try after sometime.")
            return redirect(reverse('home'))
    else:            
        return render(request,'checkout.html',{'subtotal': subtotal, 'delivery_charge': delivery_charge, 'to_pay': to_pay})
        