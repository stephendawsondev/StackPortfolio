# Generated by Django 3.2.22 on 2023-11-17 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20231117_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_active',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_date_created',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_date_updated',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_slug',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_view_count',
        ),
    ]