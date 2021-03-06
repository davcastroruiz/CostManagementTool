# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-01 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20181022_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('type', models.CharField(choices=[('boolean', 'Boolean'), ('number', 'Number'), ('text', 'Text')], default='text', max_length=255)),
            ],
        ),
    ]
