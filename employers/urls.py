from django.urls import path
from . import views

urlpatterns = [
    path('employer', views.indexE),
    path('employer/login', views.loginE),
    path('employer/SignUp', views.SignUp),
    path('employer/register', views.registerE),
    path('employer/jobs', views.registerE)
]