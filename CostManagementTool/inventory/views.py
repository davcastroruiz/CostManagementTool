# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from pymongo import MongoClient
from dashboard.models import Project


# Create your views here.
def inventory(request, d):
    project = Project.objects.get(id=d)
    connection = MongoClient('localhost', 27017)
    db = connection.Test
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
