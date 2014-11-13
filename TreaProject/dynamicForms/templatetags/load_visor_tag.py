from django import template
from django.template.loader import render_to_string
from django.conf import settings


from classytags.core import Options
from classytags.arguments import Argument
from classytags.helpers import InclusionTag

from dynamicForms.models import Form

register = template.Library()

class visor_template_tag(InclusionTag):
    """
    Template Tag to include a Form into an existing Page.
    Usage:
        {% visor_template_tag form %}
    where form is the pk of the form to be loaded.
    """
    template = 'visor_cms.html'
    options = Options(
        Argument('form'),
    )

    def get_context(self, context, form):
        output = Form.objects.get(pk=form).slug
        base_url = settings.FORMS_BASE_URL
        context['instance'] = output
        context['base_url'] = base_url    
        return context

    def render_tag(self, context, form):
        data = self.get_context(context, form)
        output = render_to_string(self.template, data)
        return output
    
register.tag(visor_template_tag)