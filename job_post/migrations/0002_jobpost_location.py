# Generated by Django 3.2.22 on 2023-11-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='location',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
