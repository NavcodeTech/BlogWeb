# Generated by Django 3.2.4 on 2021-11-21 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0015_blogmodel_total_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='total_likes',
        ),
    ]
