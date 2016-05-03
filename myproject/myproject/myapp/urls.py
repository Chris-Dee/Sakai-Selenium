# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/script/$', 'script', name='script'),
    url(r'^list/$', 'list', name='list'),
)
