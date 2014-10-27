
from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic import TemplateView
from formularios import views
from dynamicForms import views as dyn

admin.autodiscover()

urlpatterns = patterns('dynamicForms.views',
    url(r'^visor_template', TemplateView.as_view(template_name='visor_template.html')),
    url(r'^visor/publishVersion/(?P<slug>[a-z,0-9,\-,\_]+)/$', dyn.FillForm.as_view()),
    url(r'^visor$', TemplateView.as_view(template_name='visor.html')),
    url(r'^visor/submit/(?P<slug>[a-z,0-9,\-,\_]+)/$', 'submit_form_entry'),
    url(r'^visor/form/submitted/$', TemplateView.as_view(template_name='form_submitted.html')),
    url(r'^users$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^field/(?P<type>[A-Z,a-z,0-9,\-,\_]+)/$', dyn.FieldTemplateView.as_view()),
)