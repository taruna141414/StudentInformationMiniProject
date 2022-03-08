# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-10-02 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20211001_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stud_info',
            options={'verbose_name': 'Student Information', 'verbose_name_plural': "Student's Information"},
        ),
        migrations.AlterModelOptions(
            name='stud_marks',
            options={'verbose_name': "Student's Mark", 'verbose_name_plural': "Student's Marks"},
        ),
        migrations.AlterField(
            model_name='stud_info',
            name='s_address',
            field=models.CharField(max_length=200, verbose_name='Address'),
        ),
    ]
