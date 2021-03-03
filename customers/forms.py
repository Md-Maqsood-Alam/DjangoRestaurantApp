from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class profileForm(forms.Form):
    first_name=forms.CharField(
        validators=[RegexValidator(regex='^[a-zA-Z ]{2,50}$', message='Please enter a valid name')],
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'pattern': '^[a-zA-Z ]{2,50}$',
            'title': 'Name should only have alphabets and spaces, should be atleast 2 characters.',
            'required': 'required'
    }))
    last_name=forms.CharField(
        validators=[RegexValidator(regex='^[a-zA-Z ]{2,50}$', message='Please enter a valid name')],
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'pattern': '^[a-zA-Z ]{2,50}$',
            'title': 'Name should only have alphabets and spaces, should be atleast 2 characters.',
            'required': 'required'
    }))
    address=forms.CharField(max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Street Address','required': 'required'}))
    city=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City','required': 'required'}))
    state=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'State','required': 'required'}))
    country=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Country','required': 'required'}))
    zip=forms.CharField(
        max_length=6,
        validators=[RegexValidator(regex='^[0-9]{6}$', message='Please enter a valid 6 digit zip/pin code')],
        widget=forms.TextInput(attrs={
            'placeholder': 'Pincode',
            'pattern': '^[0-9]{6}$',
            'title': 'Please enter a valid 6 digits zip/pin code',
            'required': 'required'
    }))
    phone_number=forms.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^[0-9]{10}$', message='Please enter a valid 10 digit Mobile Number')],
        widget=forms.TextInput(attrs={
            'placeholder': 'Mobile Number',
            'pattern': '^[0-9]{10}$',
            'title': 'Please enter a valid 10 digits mobile number',
            'required': 'required'
    }))