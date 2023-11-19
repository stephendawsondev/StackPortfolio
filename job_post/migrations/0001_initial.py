# Generated by Django 3.2.22 on 2023-11-17 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technology', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('view_count', models.IntegerField(default=0)),
                ('company', models.CharField(blank=True, max_length=80, null=True)),
                ('salary_from', models.IntegerField(blank=True, null=True)),
                ('salary_to', models.IntegerField(blank=True, null=True)),
                ('salary_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('technologies', models.ManyToManyField(blank=True, related_name='job_posts', to='technology.Tech')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]