# Generated by Django 3.2.22 on 2023-11-17 11:46

from django.db import migrations


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
        ('project', '0006_alter_project_technologies'),
    ]

    operations = [
        migrations.RunPython(migrate_project_data),
    ]
