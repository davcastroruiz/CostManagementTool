from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
import os
import tempfile
from django.template.context_processors import csrf
from dashboard.forms import UpdateDetailsForm
from models import Theme
import xlrd
import utility


def dashboard(request):
    return render(request, 'dashboard.html')


def change_theme(request, theme):
    current_theme = Theme.objects.get(user=request.user)
    current_theme.theme = theme
    current_theme.save()
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)


def update_details(request):
    global path
    message = ''
    txt = ''
    if request.method == 'POST':
        form = UpdateDetailsForm(request.POST, request.FILES)
        if form.is_bound:
            # import your django model here like from django.appname.models import model_name
            excel_file = request.FILES['excel_file']
            initial_row = int(request.POST['initial_row'])
            final_row = int(request.POST['final_row'])
            sheet_names = str(request.POST['sheet_names'])
            if ';' not in sheet_names:
                sheet_names += ';'
            sheet_names = filter(None, sheet_names.split(';'))
            try:
                fd, path = tempfile.mkstemp()
                with os.fdopen(fd, 'wb') as tmp:
                    tmp.write(excel_file.read())
                book = xlrd.open_workbook(path)
                # sheet_names = book.sheet_names()
                for sheet_name in sheet_names:
                    txt += ('-' * 40) + '\n'
                    txt += sheet_name + '\n'
                    try:
                        sheet = book.sheet_by_name(sheet_name)
                        row = sheet.row(initial_row - 1)  # 1st row
                        headers = []
                        for idx, cell_obj in enumerate(row):
                            headers.append(cell_obj.value)

                        # Print all values, iterating through rows and columns
                        #
                        num_cols = sheet.ncols  # Number of columns
                        if final_row == 0:
                            num_rows = sheet.nrows
                        else:
                            num_rows = final_row
                        for row_idx in range(initial_row, num_rows):  # Iterate through rows
                            txt += ('-' * 40) + '\n'
                            txt += ('Row: %s' % str(row_idx + 1)) + '\n'  # Print row number
                            for col_idx in range(0, num_cols):  # Iterate through columns
                                cell_obj = sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                                txt += ('%s: %s' % (headers[col_idx], cell_obj.value)) + '\n'
                    except:
                        txt += "Invalid sheet name \n"

            finally:
                os.remove(path)
        else:
            message = 'Invalid Entries'
    dictionary = dict(request=request, message=message, txt=txt)
    dictionary.update(csrf(request))
    return render_to_response('utilities/load_excel.html', dictionary)


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
        print request.POST
    return redirect('dashboard:admin-fields')
