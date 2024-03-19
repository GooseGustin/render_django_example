from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # for flashing messages to user 
# For registration 
from django.contrib.auth.forms import UserCreationForm
from .forms import ChangePasswordForm
# 

# Create your views here.
def login_view(request): 
    if request.method == 'POST': 
        username = request.POST['username']
        # email = request.POST['email'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password) # email=email
        if user:
            login(request, user)
            print('In login view, user is logged in')
            return redirect(reverse('core:home'))
        else: 
            print('In login view, user is not logged in')
            messages.success(request, ("There was an error in logging in"))
            return redirect(reverse('authentic:login'))
    else: 
        print('In login view, user did not log in')
        return render(request, 'authentic/login.html', {}) 

def logout_view(request):
    logout(request)
    messages.success(request, ("You have been successfully logged out of the site"))
    return redirect(reverse('core:home'))

def signup_view(request):
    if request.method == 'POST': 
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # print('Form is valid')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            user = authenticate(username=username, password=password)
            login(request, user) 
            messages.success(request, ("Registration successful"))
            return redirect(reverse('core:home'))
        else: 
            form = UserCreationForm()
            messages.success(request, ("Error signing you up. Ensure your username is more than 4 characters long and password contains capital letters, numbers, special symbols and is up to 8 characters long"))
            # print('form is invalid')
    return render(request, 'authentic/signup.html')

def update_password(request):
    current_user = request.user 
    if current_user.is_authenticated: 
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ('You password has been updated. Please log in again...'))
                return redirect(reverse('authentic:login'))
            else: 
                for error in list(form.errors.values()):
                    messages.error(request, error)
                # return render()
        else:
            form = ChangePasswordForm(current_user) 
        return render(request, 'authentic/update_password.html', {'form': form})
    else:
        messages.success(request, ("You must be logged in to update your password"))
        return redirect(reverse('core:home'))
    
    