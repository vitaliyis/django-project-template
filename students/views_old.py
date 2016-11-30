# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Виталий',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрей',
         'ticket': 2123,
         'image': 'img/piv.png'},
        {'id': 3,
         'first_name': u'Тарас',
         'last_name': u'Притула',
         'ticket': 5332,
         'image': 'img/podoba3.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Students %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Students %s</h1>' % sid)

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
         'group_name': u'МтМ-21',
         'captain': u'Ячменев Олег'},
        {'id': 2,
         'group_name': u'МтМ-22',
         'captain': u'Виталий Подоба'},
        {'id': 3,
         'group_name': u'МтМ-23',
         'captain': u'Иванов Андрей'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)





