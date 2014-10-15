from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.ListField import ListField
from dynamicForms.fieldtypes import FieldFactory


class CheckboxField(ListField):
    """
    Checkbox field validator, render and analize methods
    """
    def validate(self, value, **kwargs):
        #validates multiple choices
        options = []
        for option in kwargs['options']:
            options.append(option['label'])
        values = value.split('#')
        for val in values:
            if val not in options:
                raise ValidationError("Invalid value, not among options.")

    """
    Render methods for TextField template
    """
    def render(self):
        return 'fields/checkbox/template.html'

    def render_properties(self):
        return 'fields/checkbox/properties.html'

    def __str__():
        return "Checkbox"


FieldFactory.FieldFactory.register('CheckboxField', CheckboxField)