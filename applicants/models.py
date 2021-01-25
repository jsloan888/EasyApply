from django.db import models
import re

# Create your models here.
class ApplicantManager(models.Manager):
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

class Applicant(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ApplicantManager()

class Profile(models.Model):
    applicant = models.ForeignKey(Applicant, related_name="user_profile", on_delete=models.CASCADE)
    skills = models.CharField(max_length=250)
    prev_job = models.CharField(max_length=50)
    prev_company = models.CharField(max_length=50)