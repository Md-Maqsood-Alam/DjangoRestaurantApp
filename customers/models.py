from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zip=models.CharField(max_length=6)
    phone_number=models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

    @property
    def full_address(self):
        return self.address+', '+self.city+', '+self.state+', '+self.country+'-'+self.zip+'.'

    @property
    def full_name(self):
        return self.user.first_name+' '+self.user.last_name