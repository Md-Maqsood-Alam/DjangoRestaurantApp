from django.urls import path
from .views import home, reservation, order, checkout
urlpatterns=[
    path('', home, name='home'),
    path('reservation/', reservation, name='reservation'),
    path('order/',order,name='order'),
    path('checkout/',checkout, name='checkout'),
]