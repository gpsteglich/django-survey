from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Survey, Hello, Form

from django.conf import settings

class HelloPlugin(CMSPluginBase):
    model = Hello
    name = _("Hello Plugin")
    render_template = "hello_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(HelloPlugin)

class SurveyPlugin(CMSPluginBase):
    model = Survey
    name = _("Survey Plugin")
    render_template = "visor_cms.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['base_url'] = settings.FORMS_BASE_URL
        return context

plugin_pool.register_plugin(SurveyPlugin)