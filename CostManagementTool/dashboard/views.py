from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
import os
import tempfile
from django.template.context_processors import csrf
from dashboard.forms import UpdateDetailsForm
from models import Theme
import xlrd


def index(request):
    return render(request, 'home.html')


def change_theme(request, user):
    theme = request.POST.get('theme')
    current_theme = Theme.objects.get(user=user)
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
            try:
                fd, path = tempfile.mkstemp()
                with os.fdopen(fd, 'wb') as tmp:
                    tmp.write(excel_file.read())
                book = xlrd.open_workbook(path)
                sheet_names = book.sheet_names()
                for sheet_name in sheet_names:
                    txt += ('-' * 40) + '\n'
                    txt += sheet_name + '\n'
                    sheet = book.sheet_by_name(sheet_name)
                    row = sheet.row(0)  # 1st row
                    headers = []

                    for idx, cell_obj in enumerate(row):
                        headers.append(cell_obj.value)

                    # Print all values, iterating through rows and columns
                    #
                    num_cols = sheet.ncols  # Number of columns
                    for row_idx in range(1, sheet.nrows):  # Iterate through rows
                        txt += ('-' * 40) + '\n'
                        txt += ('Row: %s' % row_idx) + '\n'  # Print row number
                        for col_idx in range(0, num_cols):  # Iterate through columns
                            cell_obj = sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                            txt += ('%s: %s' % (headers[col_idx], cell_obj.value)) + '\n'

            finally:
                os.remove(path)
        else:
            message = 'Invalid Entries'
    dictionary = dict(request=request, message=message, txt=txt)
    dictionary.update(csrf(request))
    return render_to_response('home.html', dictionary)
