# Generated by Django 3.2.4 on 2021-11-08 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0002_alter_blogmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
