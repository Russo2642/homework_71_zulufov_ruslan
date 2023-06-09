# Generated by Django 4.1.7 on 2023-03-27 10:12

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_gender_alter_account_phone'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='commented_posts',
        ),
        migrations.RemoveField(
            model_name='account',
            name='liked_posts',
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Мужской'), ('FEMALE', 'Женский')], max_length=7, verbose_name='Пол'),
        ),
    ]
