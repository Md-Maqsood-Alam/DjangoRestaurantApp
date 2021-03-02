from django.db import models
from django.contrib.auth.models import User
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
    
    def __str__(self):
        return self.name

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
