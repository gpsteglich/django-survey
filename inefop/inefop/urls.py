from django.conf.urls import patterns, include, url
import dynamicForms
from django.contrib import admin
from dynamicForms import views as dyn
admin.autodiscover()

urlpatterns = patterns('dynamicForms.views',
    # Examples:
    # url(r'^$', 'inefop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forms/', include('formularios.urls')),
    url(r'^inefop/', include('dynamicForms.urls'), name='base'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^base_url/$', dyn.get_URL),
)
