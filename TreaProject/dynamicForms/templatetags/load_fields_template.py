from django import template
from django.template.loader import render_to_string
from django.templatetags.static import static
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
        asset_list = [static('js/fields/NumberField.js'),
                    static('js/fields/TextField.js'),
                    static('js/fields/TextAreaField.js'),
                    static('js/fields/EmailField.js'),
                    static('js/fields/CheckboxField.js'),
                    static('js/fields/NumberField.js'),
                    static('js/fields/SelectField.js'),
                    static('js/fields/CIField.js'),
                    static('js/fields/Matricula.js'),
                    static('js/fields/Usuario.js'),
                    static('js/operators/operatorList.js'),
                    static('js/operators/operatorChecks.js'),
                    static('js/operators/operatorNumber.js'),
                    ]
        #asset_list = asset_block_template.get_static_field_files(self)
        context['asset_list'] = asset_list
        return context

    def render_tag(self, context):
        data = self.get_context(context)
        output = render_to_string(self.template, data)
        return output
    
register.tag(asset_block_template)