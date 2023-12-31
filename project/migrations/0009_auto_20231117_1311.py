# Generated by Django 3.2.22 on 2023-11-17 13:11

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


def migrate_project_data(apps, schema_editor):
    Project = apps.get_model('project', 'Project')
    for project in Project.objects.all():
        project.name = project.project_name
        project.active = project.project_active
        project.description = project.project_description
        project.image = project.project_image
        project.view_count = project.project_view_count
        project.slug = project.project_slug
        project.date_created = project.project_date_created
        project.date_updated = project.project_date_updated
        project.save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0008_auto_20231117_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('user', 'name')},
        ),
        migrations.RunPython(migrate_project_data),
    ]
