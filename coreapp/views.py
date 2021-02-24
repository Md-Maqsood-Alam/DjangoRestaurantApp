from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def reservation(request):
    return render(request,'reservation.html')