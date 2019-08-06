# Generated by Django 2.0.13 on 2019-08-06 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArgumentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='CommandLineArgument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('optional', models.BooleanField(default=True)),
                ('parameter', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='argumentorder',
            name='argument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.CommandLineArgument'),
        ),
        migrations.AddField(
            model_name='argumentorder',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments_order', to='tools.Tool'),
        ),
        migrations.AddField(
            model_name='tool',
            name='arguments',
            field=models.ManyToManyField(through='tools.ArgumentOrder', to='tools.CommandLineArgument'),
        ),
    ]
