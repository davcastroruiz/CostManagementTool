# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_theme_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='default', max_length=50)),
                ('owner', models.TextField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
