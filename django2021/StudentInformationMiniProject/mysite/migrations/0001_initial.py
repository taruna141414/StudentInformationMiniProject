# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-09-29 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stud_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50, unique=True)),
                ('s_address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Stud_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_marks1', models.IntegerField()),
                ('s_marks2', models.IntegerField()),
                ('s_marks3', models.IntegerField()),
                ('s_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Stud_info')),
            ],
        ),
    ]
