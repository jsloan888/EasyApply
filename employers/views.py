from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employer, EmployerManager
import bcrypt

# Create your views here.
def indexE(request):
    return render(request, "indexE.html")

def SignUpE(request):
    return render(request, "signUpE.html")

def registerE(request):
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
        return redirect('/employer/jobs')
    return redirect('/')

def jobsE(request):
    if 'companyid' in request.session:
        context = {
            'Company': Employer.objects.get(id=request.session['companyid']),
            #'all_wishes': Wish.objects.all() CHANGE TO JOBS AVAILABLE
        }
        return render(request, 'dashboardE.html', context)
    return redirect("/")

def loginE(request):
    company = Employer.objects.filter(email=request.POST['email'])
    if company:
        logged_user = company[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['companyid'] = logged_user.id
            return redirect('/employer/jobs')
    messages.error(request, "Email not found in database")
    return redirect('/employer')

def profileE(request):
    context = {
        'employer': Employer.objects.get(id=request.session['companyid']),
    }
    return render(request, 'profileE.html', context)

def logoutE(request):
    request.session.flush()
    return redirect("/employer")

def resourcesE(request):
    return render(request, "resourcesE.html")   