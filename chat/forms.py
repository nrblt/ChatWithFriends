from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from .models import *

# from .models import Order

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['msg']
