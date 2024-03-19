from django.urls import path 
from .views import (
    login_view, 
    logout_view, 
    signup_view, 
    update_password, 
)

app_name = 'authentic'

urlpatterns = [
    path('login', login_view, name='login'), 
    path('logout', logout_view, name='logout'), 
    path('signup', signup_view, name='signup'), 
    path('update_password', update_password, name='update_password')
]