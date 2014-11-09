from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Survey

from django.conf import settings

class SurveyPlugin(CMSPluginBase):
    model = Survey
    name = _("Survey Plugin")
    render_template = "visor_cms.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['base_url'] = settings.FORMS_BASE_URL
        return context

plugin_pool.register_plugin(SurveyPlugin)