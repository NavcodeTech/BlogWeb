# Generated by Django 3.2.4 on 2021-11-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0014_remove_blogmodel_tot_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
    ]
