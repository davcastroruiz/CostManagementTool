# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from pymongo import MongoClient
from dashboard.models import Project
import os
import tempfile
from django.template.context_processors import csrf
from inventory.forms import UpdateDetailsForm
import xlrd


# Create your views here.
def inventory(request, d):
    project = Project.objects.get(id=d)
    connection = MongoClient('localhost', 27017)
    db = connection.test
    pipeline = [
        {
            '$match': {
                'project': int(d)
            }
        }, {
            '$project': {
                'version': 1,
                'alias': 1,
                'created': 1,
                'createdby': 1
            }
        }
    ]
    collection = list(db.cmt.aggregate(pipeline))
    dictionary = dict(request=request, project=project, collection=collection)
    dictionary.update(csrf(request))
    return render_to_response('inventory.html', dictionary)


def update_details(request, d):
    global path
    message = ''
    txt = ''
    info = {}
    excel_translate_json = []
    if request.method == 'POST':
        form = UpdateDetailsForm(request.POST, request.FILES)
        if form.is_bound:
            # import your django model here like from django.appname.models import model_name
            excel_file = request.FILES['excel_file']
            initial_row = int(request.POST['initial_row'])
            final_row = int(request.POST['final_row'])
            info = {'alias': request.POST['alias'],
                    'version': request.POST['version']}
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
                            row_json = {}
                            for col_idx in range(0, num_cols):  # Iterate through columns
                                cell_obj = sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                                txt += ('%s: %s' % (headers[col_idx], cell_obj.value)) + '\n'
                                row_json.update({headers[col_idx]: cell_obj.value})
                            excel_translate_json.append(row_json)
                    except:
                        txt += "Invalid sheet name \n"

            finally:
                os.remove(path)
        else:
            message = 'Invalid Entries'
    project = Project.objects.get(id=d)
    dictionary = dict(request=request, message=message, txt=txt, project=project, info=info,
                      excel_translate_json=excel_translate_json)
    dictionary.update(csrf(request))
    return render_to_response('utilities/load_excel.html', dictionary)
