from django import template
from django.template.loader import render_to_string
from django.templatetags.static import static
from classytags.helpers import InclusionTag
from dynamicForms.fieldtypes import FieldFactory

register = template.Library()

class asset_block_template(InclusionTag):
    template = 'asset_block_template.html'

    def get_context(self, context):
        l = FieldFactory.FieldFactory.get_all_classes()
        ret = []
        for c in l:
            ret.extend(c.get_assets())
        context['asset_list'] = []
        for elem in ret:
        	st_elem = static(elem)
        	if st_elem not in context['asset_list']:
        		context['asset_list'].append(st_elem)
        return context

    def render_tag(self, context):
        data = self.get_context(context)
        output = render_to_string(self.template, data)
        return output
    
register.tag(asset_block_template)