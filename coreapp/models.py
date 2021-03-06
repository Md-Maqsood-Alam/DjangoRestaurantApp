from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
# Create your models here.
class Dish(models.Model):
    dishTypesChoices=(
        ('Starters','Starters'),
        ('Main Course','Main Course'),
        ('Fried Rice and Noodles','Fried Rice and Noodles'),
        ('Bread','Bread'),
        ('Rolls','Rolls'),
        ('Momos','Momos'),
        ('Soups','Soups'),
        ('Others','Others'),
        )
    name=models.CharField(max_length=100)
    dish_type=models.CharField(choices=dishTypesChoices, max_length=50)
    price=models.PositiveIntegerField()
    img=models.CharField(max_length=300)
    description=models.TextField(blank=True)
    whetherNonVeg=models.BooleanField(default=True)
    available=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class TodaysSpecials(models.Model):
    dishes=models.ManyToManyField(Dish)

class Reservation(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    num_people=models.PositiveIntegerField(default=1)
    date_and_time=models.DateTimeField()
    occasion=models.CharField(max_length=50, null=True, blank=True)
    user=models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}|{}|{}'.format(self.date_and_time,self.num_people,self.name)

class Order(models.Model):
    statusChoices=(
        ('Delivered','Delivered'),
        ('On It\'s Way','On It\'s Way'),
        ('Cancelled','Cancelled')
        )
    date_and_time=models.DateTimeField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    dishes_ordered=models.TextField()
    dishes_total=models.PositiveIntegerField()
    delivery_charge=models.PositiveIntegerField()
    delivery_address=models.TextField()
    status=models.CharField(max_length=11,choices=statusChoices, default='On It\'s Way')

    @property
    def orderId(self):
        return '{}{}{}{}'.format(
            self.date_and_time.year,
            self.date_and_time.month,
            self.user.id,
            self.id
            )

    @property
    def total_bill(self):
        return self.dishes_total+self.delivery_charge

    def __str__(self):
        return '{}|{}|{}|{}|{}|{}'.format(self.status,self.date_and_time,self.customer.full_name,self.dishes_ordered,self.total_bill,self.customer.phone_number)
