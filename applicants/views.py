from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Applicant, ApplicantManager, Profile
import bcrypt
from employers.models import Employer, EmployerManager, Job, JobManager, CompanyProfile

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signUp.html")

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
    messages.error(request, "Please enter valid email and password combination")
    return redirect('/')

def profile(request, applicantid):
    if 'userid' in request.session:
        context = {
            'applicant': Applicant.objects.get(id=applicantid),
            'all_profiles': Profile.objects.all()
        }
        return render(request, 'profile.html', context)

def editProfile(request, applicantid):
    if 'userid' in request.session:
        context = {
            'applicant': Applicant.objects.get(id=applicantid),
            'user_profile': Profile.objects.get(id=applicantid)
        }
        return render(request, 'profileEdit.html', context)

def resources(request):
    if 'userid' in request.session:
        context = {
            'applicant': Applicant.objects.get(id=request.session['userid']),
            'all_jobs': Job.objects.all()
        }
        return render(request, 'resources.html', context)
    return redirect('/')

def apply(request, jobid):
    if 'userid' in request.session:
        context = {
            'user': Applicant.objects.get(id=request.session['userid']),
            'job': Job.objects.get(id=jobid),
            'company_profile': CompanyProfile.objects.all()
        }
        return render(request, 'apply.html', context)
    return redirect('/')

def submit(request, jobid):
    user = Applicant.objects.get(id=request.session['userid'])
    posting = Job.objects.get(id=jobid)
    posting.applications.add(user)
    posting.save()
    return redirect('/jobs')

def createProfile(request, applicantid):
    user = Applicant.objects.get(id=applicantid)
    if request.method == "POST":
        profile = Profile.objects.create(
            applicant=user,
            skills=request.POST['skills'],
            prev_job=request.POST['prev_job'],
            prev_company=request.POST['prev_company'],
        )
        return redirect(f'/profile/{applicantid}')
    return redirect('/')

def updateProfile(request, applicantid):
    profUpdate = Profile.objects.get(id=applicantid)
    profUpdate.skills = request.POST['skills']
    profUpdate.prev_job = request.POST['prev_job']
    profUpdate.prev_company = request.POST['prev_company']
    profUpdate.save()
    return redirect(f'/profile/{applicantid}')

def withdraw(request, jobid):
    user = Applicant.objects.get(id=request.session['userid'])
    posting = Job.objects.get(id=jobid)
    posting.applications.remove(user)
    posting.save()
    return redirect('/jobs')