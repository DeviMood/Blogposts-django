# Generated by Django 3.2.16 on 2023-02-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0018_coment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
