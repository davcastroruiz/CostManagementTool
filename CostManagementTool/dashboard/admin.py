# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Theme, Project, Field

admin.site.register(Theme)
admin.site.register(Project)
admin.site.register(Field)
