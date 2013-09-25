# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from upload import views

urlpatterns = patterns('',
   url(r'^list/$', views.list, name='list'),
)
