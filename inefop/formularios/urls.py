
from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic import TemplateView
from formularios import views

admin.autodiscover()

urlpatterns = patterns('formularios.views',
    url(r'^visor_template', TemplateView.as_view(template_name='visor_template.html')),
    #url(r'^visor/publishVersion/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.FillForm.as_view()),
    url(r'^visor$', TemplateView.as_view(template_name='visor.html')),
    #url(r'^visor/submit/(?P<slug>[a-z,0-9,\-,\_]+)$', 'submit_form_entry'),
    url(r'^visor/form/submitted/$', TemplateView.as_view(template_name='form_submitted.html')),
    url(r'^users$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)