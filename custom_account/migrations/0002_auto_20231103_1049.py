# Generated by Django 3.2.22 on 2023-11-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentuser',
            name='first_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='parentuser',
            name='last_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='parentuser',
            name='username',
            field=models.CharField(default='testusername1', max_length=60, unique=True),
            preserve_default=False,
        ),
    ]