from django.core.exceptions import ValidationError
import re

from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes import FieldFactory


class CIField(Field.Field):
    """
    CI field type class
    """
    def check_id(self, value):
        digits = [int(i) for i in value]
        # If value has less than 8 digits, we complete with zeros on the left
        if len(digits) < 8:
            diff = 8 - len(digits)
            for x in range(0, diff + 1):
                digits.insert(0, 0)

        const = [2, 9, 8, 7, 6, 3, 4]
        value = 0
        for x in range(0, 7):
            value += digits[x] * const[x]
        m = value % 10
        if ((10 - m) % 10) != digits[len(digits) - 1]:
            raise ValidationError('Enter a valid ID.', code='invalid')

    def validate(self, value, **kwargs):
        #default validation or pass
        super(CIField, self).validate(value, **kwargs)
        intvalue = re.sub('[.-]', '', value)
        try:
            int(intvalue)
        except (ValueError, TypeError):
            raise ValidationError('Enter a valid integer.', code='invalid')
        self.check_id(intvalue)
        return True

    """
    Render methods for CIField template
    """
    def render(self):
        return 'fields/identity_doc/template.html'
    
    def render_edit(self):
        return 'fields/identity_doc/template_edit.html'

    def render_properties(self):
        return 'fields/identity_doc/properties.html'

    def __str__():
        return "Cedula"


FieldFactory.FieldFactory.register('CIField', CIField)