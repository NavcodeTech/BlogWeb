# Generated by Django 3.2.4 on 2021-11-19 09:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0010_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='likes',
            field=models.ManyToManyField(related_name='liked_blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
