from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employer, EmployerManager, Job, JobManager, CompanyProfile
import bcrypt
from applicants.models import Applicant, ApplicantManager, Profile

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
        return redirect('/employer/signup')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/employer/signup')
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
    return redirect('/employer/signup')

def jobsE(request):
    if 'companyid' in request.session:
        context = {
            'company': Employer.objects.get(id=request.session['companyid']),
            'all_jobs': Job.objects.all(),
            'all_profiles': Profile.objects.all()
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
    if 'companyid' in request.session:
        context = {
            'employer': Employer.objects.get(id=request.session['companyid']),
            'all_jobs': Job.objects.all(),
            'company_profiles': CompanyProfile.objects.all()
        }
        return render(request, 'profileE.html', context)
    return redirect('/')

def logoutE(request):
    request.session.flush()
    return redirect("/employer")

def newJob(request):
    if 'companyid' in request.session:
        context = {
            'employer': Employer.objects.get(id=request.session['companyid']),
            'all_jobs': Job.objects.all()
        }
        return render(request, 'addJob.html', context)
    return redirect('/')

def addJob(request):
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/employer/addJob')
    user = Employer.objects.get(id=request.session['companyid'])
    job = Job.objects.create(
        title=request.POST['title'],
        experience=request.POST['experience'],
        skills=request.POST['skills'],
        description=request.POST['desc'],
        uploaded_by=user
    )
    return redirect ('/employer/addJob')

def editJob(request, jobid):
    if 'companyid' in request.session:
        context = {
            'company': Employer.objects.get(id=request.session['companyid']),
            'job': Job.objects.get(id=jobid)
        }
        return render(request, 'updateJob.html', context)
    return redirect('/')

def update(request, jobid):
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/employer/{jobid}')
    job = Job.objects.get(id=jobid)
    job.title = request.POST['title']
    job.experience = request.POST['experience']
    job.skills = request.POST['skills']
    job.description = request.POST['desc']
    job.save()
    return redirect('/employer/addJob')

def profUpdate(request):
    if 'companyid' in request.session:
        user=Employer.objects.get(id=request.session['companyid'])
        profile = CompanyProfile.objects.create(
            company=user,
            employee_count=request.POST['employees'],
            corp_hq=request.POST['headquarters'],
            description=request.POST['description']
        )
        return redirect ('/employer/profile')    
    else:
        return redirect('/')

def hire(request, jobid, applicantid):
    hired_job = Job.objects.get(id=jobid)
    hired_job.hired = True
    hired_applicant = Applicant.objects.get(id=applicantid)
    hired_job.hiree.add(hired_applicant)
    hired_job.save()
    return redirect('/employer/jobs')

def unhire(request, jobid, applicantid):
    hired_job = Job.objects.get(id=jobid)
    hired_job.hired = False
    unhired_applicant = Applicant.objects.get(id=applicantid)
    hired_job.hiree.add(unhired_applicant)
    hired_job.save()
    return redirect('/employer/jobs')