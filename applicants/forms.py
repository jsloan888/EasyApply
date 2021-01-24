from django import forms

class Profile2(forms.Form):
    resume = forms.FileField()