'''
Created on 30/8/2014

@author: federico
'''
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from dynamicForms import views 
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]
    
    def get(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.user.is_anonymous():
            # Auto-login the User for Demonstration Purposes
            user = authenticate()
            login(request, user)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)

urlpatterns = patterns('dynamicForms.views',
    url(r'(?P<pk>[0-9]+)/$', views.FormDetail.as_view()),
    url(r'^list/$', views.FormList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^visorTest$', TemplateView.as_view(template_name='visorTest.html')),
    url(r'^visor$', TemplateView.as_view(template_name='visor.html')),
    url(r'^editor$', TemplateView.as_view(template_name='editor.html')),
    url(r'^text$', TemplateView.as_view(template_name='question_char.html')),
    url(r'^textarea$', TemplateView.as_view(template_name='question_text_area.html')),
    url(r'^number$', TemplateView.as_view(template_name='question_num.html')),
    url(r'^modify_input$', TemplateView.as_view(template_name='modifyInput.html')),

)

urlpatterns = format_suffix_patterns(urlpatterns)
