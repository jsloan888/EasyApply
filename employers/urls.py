from django.urls import path
from . import views

urlpatterns = [
    path('employer', views.indexE),
    path('employer/SignUp', views.SignUp)
]