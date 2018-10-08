# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Theme


def index(request):
    return render(request, 'base.html')


def change_theme(request, user):
    theme = request.POST.get('theme')
    current_theme = Theme.objects.get(user=user)
    current_theme.theme = theme
    current_theme.save()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)