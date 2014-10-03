'''
Created on 30/8/2014

@author: federico
'''


from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from dynamicForms import views, login,logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('dynamicForms.views',
    url(r'^forms/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.FormDetail.as_view()),
    url(r'^form/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.GetTitle.as_view()),
    url(r'^forms/delete/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.DeleteForm.as_view()),
    url(r'^forms/$', views.FormList.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/(?P<action>[a-z]+)/$', views.NewVersion.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.VersionList.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', views.VersionDetail.as_view()),
    url(r'^version/delete/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', views.DeleteVersion.as_view()),
    #url(r'^users/$', views.UserList.as_view()),
    url(r'^main/', views.FormList.as_view()),
    url(r'^newForm/', views.TemplateView.as_view(template_name= 'newForm.html')),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^login/$', login.user_login, name='login'),
    url(r'^logout/$', logout.user_logout, name='logout'),
    url(r'^visorTest$', views.TemplateView.as_view(template_name='visorTest.html')),
    #url(r'^visor$', TemplateView.as_view(template_name='visor.html')),
    url(r'^templates/(?P<template_name>\w+)/$', views.SimpleStaticView.as_view()),
    url(r'^preview$', views.TemplateView.as_view(template_name='preview.html')),
    url(r'^editor$', views.TemplateView.as_view(template_name='editor.html')),
    url(r'^field/(?P<type>[0-9]+)/$', views.FieldTemplateView.as_view()),
    url(r'^text$', views.TemplateView.as_view(template_name='question_char.html')),
    url(r'^textarea$', views.TemplateView.as_view(template_name='question_text_area.html')),
    url(r'^number$', views.TemplateView.as_view(template_name='question_num.html')),
    url(r'^identityDoc$', views.TemplateView.as_view(template_name='field_identityDoc.html')),
    url(r'^combobox$', views.TemplateView.as_view(template_name='field_combobox.html')),
    url(r'^mail$', views.TemplateView.as_view(template_name='field_mail.html')),
    url(r'^palette$', views.TemplateView.as_view(template_name='palette.html')),
    url(r'^select_modal$', views.TemplateView.as_view(template_name='select_modal.html')),
    url(r'^modify_input$', views.TemplateView.as_view(template_name='modifyInput.html')),
    url(r'^visor_template', views.TemplateView.as_view(template_name='visor_template.html')),
    url(r'^visor/publishVersion/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.FillForm.as_view()),
    url(r'^visorPub/(?P<slug>[a-z,0-9,\-,\_]+)/submit/$', 'submit_form_entry'),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/identityDoc$', views.TemplateView.as_view(template_name='field_identityDoc.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/mail$', views.TemplateView.as_view(template_name='field_mail.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/combobox$', views.TemplateView.as_view(template_name='field_combobox.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/text$', views.TemplateView.as_view(template_name='question_char.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/textarea$', views.TemplateView.as_view(template_name='question_text_area.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/number$', views.TemplateView.as_view(template_name='question_num.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.TemplateView.as_view(template_name='visor.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/formTemplate.html(.*)$', views.TemplateView.as_view(template_name='formTemplate.html')),
    url(r'^responses/(?P<slug>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', 'get_responses'),
    url(r'^responses/$', views.TemplateView.as_view(template_name='responses.html')),
    url(r'^constants/$', 'get_constants'),
    
)

urlpatterns = format_suffix_patterns(urlpatterns)
