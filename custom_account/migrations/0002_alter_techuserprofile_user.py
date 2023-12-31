# Generated by Django 3.2.22 on 2023-11-06 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techuserprofile',
            name='user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='tech_profile',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
