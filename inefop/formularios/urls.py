
from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic import TemplateView
from formularios import views
from dynamicForms import views as dyn

admin.autodiscover()

urlpatterns = patterns('dynamicForms.views',
    url(r'^users$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^clubs$', views.ClubList.as_view()),
    url(r'^club/(?P<pk>[0-9]+)/$', views.ClubDetail.as_view()),
    url(r'^countrys$', views.CountryList.as_view()),
    url(r'^country/(?P<pk>[0-9]+)/$', views.CountryDetail.as_view()),
)