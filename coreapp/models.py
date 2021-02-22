from django.db import models

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
