from django.forms import ModelForm,forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"