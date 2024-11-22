# todo/urls.py
from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),  # Make sure 'name' is 'register'
]
