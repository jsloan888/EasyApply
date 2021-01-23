# Generated by Django 2.2 on 2021-01-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0001_initial'),
        ('employers', '0004_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='applications',
            field=models.ManyToManyField(related_name='job_applicants', to='applicants.Applicant'),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]