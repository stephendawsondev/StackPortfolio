# Generated by Django 3.2.22 on 2023-11-11 21:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0004_auto_20231111_2026'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('user', 'project_name')},
        ),
    ]