# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-11 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20181109_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='type',
        ),
    ]
