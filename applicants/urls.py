from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('SignUp', views.SignUp),
    path('register', views.register)
]