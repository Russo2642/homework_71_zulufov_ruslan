# Generated by Django 4.1.7 on 2023-04-20 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
