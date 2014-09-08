'''
Created on 30/8/2014

@author: federico
'''
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from dynamicForms import views 
from django.contrib.messages.tests.urls import TEMPLATE
from django.views.generic.base import TemplateView
from rest_framework.urls import template_name

urlpatterns = patterns('dynamicForms.views',
    url(r'(?P<pk>[0-9]+)/$', views.FormDetail.as_view()),
  #  url(r'$', views.FormList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^index.html', TemplateView.as_view(template_name= 'mainPage.html')),
)

urlpatterns = format_suffix_patterns(urlpatterns)