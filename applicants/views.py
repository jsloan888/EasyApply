from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Applicant, ApplicantManager
import bcrypt
from employers.models import Employer, EmployerManager, Job, JobManager

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
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
        return redirect('/jobs')
    return redirect('/')

def jobs(request):
    if 'userid' in request.session:
        context = {
            'applicant': Applicant.objects.get(id=request.session['userid']),
            'all_jobs': Job.objects.all()
        }
        return render(request, 'dashboard.html', context)
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")

def login(request):
    user = Applicant.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/jobs')
    messages.error(request, "Email not found in database")
    return redirect('/')

def profile(request):
    context = {
        'applicant': Applicant.objects.get(id=request.session['userid']),
    }
    return render(request, 'profile.html', context)

def resources(request):
    return render(request, "resources.html")

def apply(request):
    return render(request, 'apply.html')