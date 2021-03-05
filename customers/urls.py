from django.urls import path
from .views import profileView, myaccount
urlpatterns=[
    path('profileCreate/',profileView,name='profile_create'),
    path('profileUpdate/',profileView,name='profile_update'),
    path('myaccount/',myaccount, name='myaccount')
    ]