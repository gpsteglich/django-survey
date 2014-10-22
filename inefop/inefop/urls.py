from django.conf.urls import patterns, include, url
import dynamicForms
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('dynamicForms.views',
    # Examples:
    # url(r'^$', 'inefop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forms/', include('formularios.urls')),
    url(r'^dyn/', include('dynamicForms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
