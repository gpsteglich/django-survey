from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.ListField import ListField
from dynamicForms.fieldtypes import FieldFactory

class SelectField(ListField):
    """
    Combobox field validator, render and analize methods
    """
    template_name = "combobox/template.html"
    edit_template_name = "combobox/template_edit.html"
    prp_template_name = "combobox/properties.html"

    def validate(self, value, **kwargs):
        options = []
        for option in kwargs['options']:
            options.append(option)
        if value not in options:
            raise ValidationError("Invalid value, not among options.")

    def __str__():
        return "Combo Box"


FieldFactory.FieldFactory.register('SelectField', SelectField)