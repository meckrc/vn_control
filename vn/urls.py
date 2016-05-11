# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import Hello, mftp_log
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
#    url(r'^$', Hello, name='index'),
    url(r'^$', mftp_log, name='mftp_log'),
)

