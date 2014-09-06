'''
Created on 30/8/2014

@author: federico
'''
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from dynamicForms import views 

urlpatterns = patterns('dynamicForms.views',
    url(r'^forms/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.FormDetail.as_view()),
    url(r'^forms/$', views.FormList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)