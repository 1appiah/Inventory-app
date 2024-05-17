from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class RegistForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', 
            'email',
            'password1',
            'password2'
        ]

class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model =  User
        fields = ['username', 'email',]      
         

class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model =  Profile
        fields = ['phone', 'address', 'image']  
         
