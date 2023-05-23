from django import forms 
from .models import Contact,Buyer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']

class BuyerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'pix']
        