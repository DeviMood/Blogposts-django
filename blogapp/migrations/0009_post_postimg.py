# Generated by Django 3.2.16 on 2023-02-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_remove_post_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postimg',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]