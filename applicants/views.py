from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def SignUp(request):
    return render(request, "signUp.html")

# Update to Employer/Applicant, not user
def register(request):
    if request.method == "POST":
        errors = Applicant.objects.basic_validator(request.POST)
    if Applicant.objects.filter(email = request.POST['email']):
        messages.error(request, "Email is already registered and can be used to login.")
        return redirect('/')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = Applicant.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'], 
            password=pw_hash
        )
        request.session['userid'] = new_user.id 
        return redirect('/wishes')
    return redirect('/')