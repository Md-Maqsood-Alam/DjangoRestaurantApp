from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from .forms import profileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
# Create your views here.
@login_required
def profileView(request):
    user=User.objects.get(id=request.user.id)
    if request.method=='POST':
        form=profileForm(request.POST)
        if form.is_valid():
            cleanedData=form.cleaned_data
            user.first_name=cleanedData['first_name']
            user.last_name=cleanedData['last_name']
            user.save()
            if request.path==reverse('profile_update'):
                customer=user.customer
                customer.address=cleanedData['address']
                customer.city=cleanedData['city']
                customer.state=cleanedData['state']
                customer.country=cleanedData['country']
                customer.zip=cleanedData['zip']
                customer.phone_number=cleanedData['phone_number']
            else:
                customer=Customer(
                    user=user,
                    address=cleanedData['address'],
                    city=cleanedData['city'],
                    state=cleanedData['state'],
                    country=cleanedData['country'],
                    zip=cleanedData['zip'],
                    phone_number=cleanedData['phone_number'],
                    )
            customer.save()
            messages.add_message(request, messages.INFO, 'Your details were updated successfully.')
            return redirect(reverse('home'))
    else:
        if request.path==reverse('profile_update'):
            customer=user.customer
            form=profileForm(initial={
                'first_name': customer.user.first_name,
                'last_name': customer.user.last_name,
                'address': customer.address,
                'city': customer.city,
                'state': customer.state,
                'country': customer.country,
                'zip': customer.zip,
                'phone_number': customer.phone_number
                })
        else:
            form=profileForm()
    return render(request,'profile.html',{'form':form})