from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User 
from django import forms 

class ChangePasswordForm(SetPasswordForm):
    class Meta: 
        model = User 
        fields = [
            'new_password1', 
            'new_password2'
        ]

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50) 
    
    class Meta: 
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name'
        ]
