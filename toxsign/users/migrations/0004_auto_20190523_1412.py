# Generated by Django 2.0.13 on 2019-05-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('users', '0003_user_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='projects',
        ),
        migrations.AddField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(related_name='projects', to='projects.Project'),
        ),
    ]
