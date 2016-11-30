# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Visits
def visits_list(request):

    return render(request, 'students/visits_list.html', {})