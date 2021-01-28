from django.urls import path
from . import views

urlpatterns = [
    path('employer', views.indexE),
    path('employer/login', views.loginE),
    path('employer/signup', views.SignUpE),
    path('employer/register', views.registerE),
    path('employer/jobs', views.jobsE),
    path('employer/profile', views.profileE),
    path('employer/logout', views.logoutE),
    path('employer/addJob', views.newJob),
    path('employer/createJob', views.addJob),
    path('employer/<int:jobid>', views.editJob),
    path('employer/<int:jobid>/editJob', views.update),
    path('employer/update', views.profCreate),
    path('employer/update/<int:companyprofileid>', views.profEdit),
    path('employer/update/<int:companyprofileid>/edit', views.profUpdate),
    path('employer/hire/<int:jobid>/<int:applicantid>', views.hire),
    path('employer/unhire/<int:jobid>/<int:applicantid>', views.unhire)
]