# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-09 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20181107_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='fields',
            field=models.ManyToManyField(blank=True, to='dashboard.Field'),
        ),
    ]
