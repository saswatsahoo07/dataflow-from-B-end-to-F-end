from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('Register', register, name='register'),
    path('users',users,name='users'),
]