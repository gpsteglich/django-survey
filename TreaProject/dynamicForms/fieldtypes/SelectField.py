from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.Field import Field
from dynamicForms.fieldtypes import FieldFactory


class SelectField(Field):
    """
    Combobox field validator, render and analize methods
    """

    def validate(self, value, **kwargs):
        options = []
        for option in kwargs['options']:
            options.append(option)
        if value not in options:
            raise ValidationError("Invalid value, not among options.")

    """
    Render methods for TextField template
    """
    def render(self):
        return 'fields/combobox/template.html'

    def render_properties(self):
        return 'fields/combobox/properties.html'

    def __str__():
        return "Combo Box"


FieldFactory.FieldFactory.register('SelectField', SelectField)