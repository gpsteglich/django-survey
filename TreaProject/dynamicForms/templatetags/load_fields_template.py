import datetime
from django import template

from dynamicForms.fieldtypes import FieldFactory

register = template.Library()


def get_static_field_files():
    l = FieldFactory.FieldFactory.get_all_classes()
    ret = ['js/fields/FieldBase.js']
    for c in l:
    	ret.extend(c.get_assets())
    return ret

register.tag('load_fields_template', get_static_field_files)