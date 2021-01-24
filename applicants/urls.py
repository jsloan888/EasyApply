from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('register', views.register),
    path('login', views.login),
    path('jobs', views.jobs),
    path('profile/<int:applicantid>', views.profile),
    path('profile/<int:applicantid>/edit', views.editProfile),
    path('logout', views.logout),
    path('resources', views.resources),
    path('apply/<int:jobid>', views.apply),
    path('apply/<int:jobid>/submit', views.submit),
    path('withdraw/<int:jobid>', views.withdraw)
]