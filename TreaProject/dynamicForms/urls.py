'''
Created on 30/8/2014

@author: federico
'''
from django.conf.urls import patterns, url

from dynamicForms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)