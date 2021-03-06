"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
#from students import views
from students.views import students, groups, visits
from .settings import MEDIA_ROOT, DEBUG, MEDIA_URL

urlpatterns = [
    # Students urls
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students.students_delete, name='students_delete'),

    # Groups urls
    url(r'groups/$', groups.groups_list, name='groups'),
    url(r'groups/add/$', groups.groups_add, name='groups_add'),
    url(r'groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),

    # Journal urls
    url(r'^journal/$', visits.visits_list, name='journal'),

    url(r'^admin/', include(admin.site.urls)),
]
if DEBUG:
    # serve files from media folder
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
       # url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT})

#urlpatterns = patterns('',
#    # Students urls
#    url(r'^$', 'students.views.students_list', name='home'),

#    url(r'^admin/', include(admin.site.urls)),
#)
