from django.urls import path
from .views import home, reservation
urlpatterns=[
    path('', home, name='home'),
    path('reservation/', reservation, name='reservation'),
]