from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from decorator_include import decorator_include


def index(request):
    return HttpResponse('Index!')


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^include/', decorator_include(login_required, 'decorator_include.tests.included')),
]
