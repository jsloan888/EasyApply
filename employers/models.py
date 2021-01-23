from django.db import models
import re
from applicants.models import Applicant

# Create your models here.
class EmployerManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2: #characters for first name
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2: #characters for last name
            errors['last_name'] = "Last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8: #characters for password
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_pw']:
            errors['password'] = "Passwords do not match"
        return errors
    def login_validator(self, postData):
        pass

class Employer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmployerManager()

class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title cannot be blank."
        if len(postData['experience']) < 1:
            errors['experience'] = "Experience cannot be blank."
        if len(postData['skills']) < 2:
            errors['skills'] = "Skills cannot be blank."
        if len(postData['desc']) < 2:
            errors['desc'] = "Description cannot be blank."
        return errors
        

class Job(models.Model):
    title = models.CharField(max_length=150)
    experience = models.CharField(max_length=50)
    skills = models.CharField(max_length=150)
    description = models.TextField()
    uploaded_by = models.ForeignKey(Employer, related_name="jobs_uploaded", on_delete=models.CASCADE)
    hired = models.BooleanField(null=True)
    hiree = models.ForeignKey(Applicant, related_name="hired_applicant", null=True, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    hired_on = models.DateField(auto_now=True, null=True)
    objects = JobManager()