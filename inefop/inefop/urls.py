from django.conf.urls import patterns, include, url
import dynamicForms
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^forms/', include('formularios.urls')),
    url(r'^inefop/', include('dynamicForms.urls'), name='base'),
    url(r'^admin/', include(admin.site.urls)),
    
    # ejemplo de un formulario publicado en una url
    url(r'^some_form/$', 'dynamicForms.views.render_form', {'instance':'ppp'}),
    
    url(r'^', include('cms.urls')),
)
