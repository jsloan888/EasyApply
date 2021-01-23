# Generated by Django 2.2 on 2021-01-23 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applicants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('experience', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=150)),
                ('hired', models.BooleanField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('hired_on', models.DateField(auto_now=True, null=True)),
                ('hiree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hired_applicant', to='applicants.Applicant')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_uploaded', to='employers.Employer')),
            ],
        ),
    ]
