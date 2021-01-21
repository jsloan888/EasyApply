from django.urls import path
from . import views

urlpatterns = [
    path('employer', views.indexE),
    path('employer/login', views.loginE),
    path('employer/SignUp', views.SignUpE),
    path('employer/register', views.registerE),
    path('employer/jobs', views.jobsE),
    path('employer/profile', views.profileE),
    path('employer/logout', views.logoutE),
    path('employer/resources', views.resourcesE)
]