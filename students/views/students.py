# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Student, Group

# Views for Students
def students_list(request):
    '''
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
    '''
    #students = Student.objects.all()
    students = Student.objects.order_by('last_name')

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:

            # errors collection
            errors = {}
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Имя должно быть обязательно"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Фамилия должна быть обязательно"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата рождения должна быть обязательно"
            else:
                data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер билета должен быть обязательно"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Выберите группу для студента"
            else:
                data['student_group'] = Group.objects.get(pk=student_group)

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # save student
            if not errors:
                # create student object
                student = Student(**data)
                # save it to database
                student.save()

                # redirect user to students list
                return HttpResponseRedirect(reverse('home'))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                              'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
                  {'groups': Group.objects.all().order_by('title')})



def students_edit(request, sid):
    return HttpResponse('<h1>Edit Students %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Students %s</h1>' % sid)