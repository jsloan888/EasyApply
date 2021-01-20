from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def indexE(request):
    return render(request, "indexE.html")

def SignUp(request):
    return render(request, "signUpE.html")

def register(request):
    if request.method == "POST":
        errors = Employer.objects.basic_validator(request.POST)
    if Employer.objects.filter(email = request.POST['email']):
        messages.error(request, "Email is already registered and can be used to login.")
        return redirect('/')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_corp = Employer.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'], 
            password=pw_hash,
            company=request.POST['company']
        )
        request.session['companyid'] = new_corp.id 
        return redirect('/wishes')
    return redirect('/')