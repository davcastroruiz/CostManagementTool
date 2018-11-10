from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from models import Theme, Project
import utility


def dashboard(request):
    return render(request, 'dashboard.html')


def change_theme(request, theme):
    current_theme = Theme.objects.get(user=request.user)
    current_theme.theme = theme
    current_theme.save()
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)


def save_project(request):
    if request.method == 'POST':
        utility.save_project(name=request.POST['projectName'], owner=request.POST['projectOwner'],
                             email='default@gmail.com')
    return redirect('dashboard:index')


def remove_project(request):
    if request.method == 'POST':
        utility.remove_project(_id=request.POST['projectId'])
    return redirect('dashboard:index')


def fields(request):
    return render(request, 'admin/fields.html')


def save_field(request):
    if request.method == 'POST':
        utility.save_field(name=request.POST['fieldName'], type_field=request.POST['fieldType'],
                           description=request.POST['fieldDescription'])
    return redirect('dashboard:admin-fields')


def remove_field(request):
    if request.method == 'POST':
        utility.remove_field(_id=request.POST['fieldId'])
    return redirect('dashboard:admin-fields')


def assign_fields(request):
    if request.method == 'POST':
        project = Project.objects.get(id=int(request.POST['project']))
        project.fields.clear()
        try:
            results = map(int, request.POST.getlist('fields'))
            for i in results:
                project.fields.add(i)
        except:
            print 'request_post for fields was empty'
        project.save()
    return redirect('dashboard:admin-fields')
