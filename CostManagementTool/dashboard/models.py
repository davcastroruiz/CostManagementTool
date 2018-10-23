# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
from bootstrap_themes import list_themes
from django.contrib.auth.models import User


class Theme(models.Model):
    # required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True)

    # additional fields
    theme = models.CharField(max_length=255, default='default', choices=list_themes())

    def __str__(self):
        return self.user.username + ' is using: ' + self.theme


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50, default='default')
    owner = models.TextField(max_length=50, blank=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.owner + ': ' + self.name
