from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from coreapp.models import Dish
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required
def cart_add(request, id):
    cart = Cart(request)
    dish = Dish.objects.get(id=id)
    cart.add(product=dish)
    return redirect(reverse('order'))


@login_required
def item_clear(request, id):
    cart = Cart(request)
    dish = Dish.objects.get(id=id)
    cart.remove(dish)
    return redirect(reverse('order'))


@login_required
def item_increment(request, id):
    cart = Cart(request)
    dish = Dish.objects.get(id=id)
    cart.add(product=dish)
    return redirect(reverse('order'))


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    dish = Dish.objects.get(id=id)
    cart.decrement(product=dish)
    return redirect(reverse('order'))


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(reverse('order'))


@login_required
def cart_clear_silent(request):
    cart = Cart(request)
    cart.clear()
