from django import template
from django.template.loader import render_to_string
from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import InclusionTag
from dynamicForms.fieldtypes import FieldFactory

register = template.Library()

class asset_block_template(InclusionTag):
    template = 'asset_block_template.html'

    def get_static_field_files(self):
        l = FieldFactory.FieldFactory.get_all_classes()
        ret = ['js/fields/FieldBase.js']
        for c in l:
            ret.extend(c.get_assets())
        return ret

    def get_context(self, context):
        asset_list = ['js/fields/NumberField.js',
                    'js/fields/TextField.js',
                    'js/fields/TextAreaField.js',
                    'js/fields/EmailField.js',
                    'js/fields/CheckboxField.js',
                    'js/fields/NumberField.js',
                    'js/fields/SelectField.js',
                    'js/fields/CIField.js',
                    'js/fields/Matricula.js',
                    'js/fields/Usuario.js',
                    'js/operators/operatorList.js',
                    'js/operators/operatorChecks.js',
                    'js/operators/operatorNumber.js',
                    ]
        #asset_list = asset_block_template.get_static_field_files(self)
        context['asset_list'] = asset_list
        return context

    def render_tag(self, context):
        data = self.get_context(context)
        output = render_to_string(self.template, data)
        return output
    
register.tag(asset_block_template)