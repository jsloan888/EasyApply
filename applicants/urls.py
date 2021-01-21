from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('SignUp', views.SignUp),
    path('register', views.register),
    path('login', views.login),
    path('jobs', views.jobs),
    path('profile', views.profile),
    path('logout', views.logout),
    path('resources', views.resources)
]