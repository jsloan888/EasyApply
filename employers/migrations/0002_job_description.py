# Generated by Django 2.2 on 2021-01-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]