from django.urls import path
from .views import profileView
from django.views.generic import TemplateView
urlpatterns=[
    path('profileCreate/',profileView,name='profile_create'),
    path('profileUpdate/',profileView,name='profile_update'),
    path('myaccount/',TemplateView.as_view(template_name='myaccount.html'), name='myaccount')
    ]