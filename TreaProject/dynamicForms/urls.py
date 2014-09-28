'''
Created on 30/8/2014

@author: federico
'''


from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from dynamicForms import views, login,logout
from django.contrib import admin

admin.autodiscover()
from django.views.generic import TemplateView
from django.shortcuts import redirect


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
    url(r'^forms/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.FormDetail.as_view()),
    url(r'^form/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.GetTitle.as_view()),
    url(r'^forms/delete/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.DeleteForm.as_view()),
    url(r'^forms/$', views.FormList.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/(?P<action>[a-z]+)/$', views.NewVersion.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/$', views.VersionList.as_view()),
    url(r'^version/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', views.VersionDetail.as_view()),
    url(r'^version/delete/(?P<pk>[a-z,0-9,\-,\_]+)/(?P<number>[0-9]+)/$', views.DeleteVersion.as_view()),
    #url(r'^users/$', views.UserList.as_view()),
    url(r'^main/', views.formList, name='main'),
    url(r'^newForm/', TemplateView.as_view(template_name= 'newForm.html')),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^login/$', login.user_login, name='login'),
    url(r'^logout/$', logout.user_logout, name='logout'),
    url(r'^visorTest$', TemplateView.as_view(template_name='visorTest.html')),
    #url(r'^visor$', TemplateView.as_view(template_name='visor.html')),
    url(r'^editor$', views.editor, name='editor'),
    url(r'^text$', TemplateView.as_view(template_name='question_char.html')),
    url(r'^textarea$', TemplateView.as_view(template_name='question_text_area.html')),
    url(r'^number$', TemplateView.as_view(template_name='question_num.html')),
    url(r'^identityDoc$', TemplateView.as_view(template_name='field_identityDoc.html')),
    url(r'^combobox$', TemplateView.as_view(template_name='field_combobox.html')),
    url(r'^mail$', TemplateView.as_view(template_name='field_mail.html')),
    url(r'^palette$', TemplateView.as_view(template_name='palette.html')),
    url(r'^select_modal$', TemplateView.as_view(template_name='select_modal.html')),
    url(r'^modify_input$', TemplateView.as_view(template_name='modifyInput.html')),
    url(r'^visor/publishVersion/(?P<slug>[a-z,0-9,\-,\_]+)/$', views.FillForm.as_view()),
    url(r'^visorPub/(?P<slug>[a-z,0-9,\-,\_]+)/submit/$', 'submit_form_entry'),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/identityDoc$', TemplateView.as_view(template_name='field_identityDoc.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/mail$', TemplateView.as_view(template_name='field_mail.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/combobox$', TemplateView.as_view(template_name='field_combobox.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/text$', TemplateView.as_view(template_name='question_char.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/textarea$', TemplateView.as_view(template_name='question_text_area.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/number$', TemplateView.as_view(template_name='question_num.html')),
    url(r'^visor/(?P<slug>[a-z,0-9,\-,\_]+)/$', TemplateView.as_view(template_name='visor.html')),
)

urlpatterns = format_suffix_patterns(urlpatterns)
