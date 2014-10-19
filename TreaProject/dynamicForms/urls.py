'''
Created on 30/8/2014

@author: federico
'''


from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from dynamicForms import views, auth
from dynamicForms.fieldtypes.field_type import on_startup
from django.contrib import admin

admin.autodiscover()

on_startup()

urlpatterns = patterns('dynamicForms.views',

    url(r'^forms/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.FormDetail.as_view()),
    url(r'^forms/delete/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.DeleteForm.as_view()),
    url(r'^forms/$', views.FormList.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/(?P<action>[a-z]+)/$', views.NewVersion.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.VersionList.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', views.VersionDetail.as_view()),
    url(r'^version/delete/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', views.DeleteVersion.as_view()),

    url(r'^main/(?P<order>(id|owner|title|creation_date))/(?P<ad>(asc|dsc))/$', 'ordered_forms', name='main'),
    url(r'^main/$', views.FormList.as_view()),
    url(r'^login/$', auth.user_login, name='login'),
    url(r'^logout/$', auth.user_logout, name='logout'),
    url(r'^preview$', views.TemplateView.as_view(template_name='preview.html')),
    url(r'^editor$', views.TemplateView.as_view(template_name='editor.html')),

    
    url(r'^field_condition$', views.TemplateView.as_view(template_name='field_condition.html')),
    url(r'^logic_modal', views.TemplateView.as_view(template_name='logic_modal.html')),
    url(r'^field/(?P<type>[A-Z,a-z,0-9,\-,\_]+)/$', views.FieldTemplateView.as_view()),
    url(r'^field_edit/(?P<type>[A-Z,a-z,0-9,\-,\_]+)/$', views.FieldEditTemplateView.as_view()),
    url(r'^field_properties/(?P<type>[A-Z,a-z,0-9,\-,\_]+)/$', views.FieldPrpTemplateView.as_view()),
    url(r'^palette$', views.TemplateView.as_view(template_name='palette.html')),
    url(r'^select_modal$', views.TemplateView.as_view(template_name='select_modal.html')),
    url(r'^tooltip_modal$', views.TemplateView.as_view(template_name='tooltip_modal.html')),
    url(r'^modify_input$', views.TemplateView.as_view(template_name='modifyInput.html')),
   
    url(r'^statistics/$' ,views.TemplateView.as_view(template_name='statistics.html')),
    url(r'^statistica/(?P<pk>[0-9]+)/(?P<number>[0-9]+)/$','getStatistics'), 
    
    url(r'^visor_template', views.TemplateView.as_view(template_name='visor_template.html')),
    url(r'^visor/publishVersion/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.FillForm.as_view()),
    url(r'^visor$', views.TemplateView.as_view(template_name='visor.html')),
    url(r'^visor/submit/(?P<slug>[a-z,0-9,\-,\_]+)$', 'submit_form_entry'),
    url(r'^visor/form/submitted/$', views.TemplateView.as_view(template_name='form_submitted.html')),

    url(r'^responses/(?P<slug>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', 'get_responses'),
    url(r'^responses/$', views.TemplateView.as_view(template_name='responses.html')),
    url(r'^constants/$', 'get_constants'),
    url(r'^pct/(?P<pk>[0-9]+)/(?P<number>[0-9]+)/(?P<field_id>[0-9]+)$', 'get_pct'),

)

urlpatterns = format_suffix_patterns(urlpatterns)
