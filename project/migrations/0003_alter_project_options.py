# Generated by Django 3.2.22 on 2023-11-11 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_technologies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-project_date_created']},
        ),
    ]
