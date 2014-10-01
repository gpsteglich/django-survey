from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.Field import validator

class TextFieldValidator(validator.FieldValidator):
    """
    Text field validator
    """
    def __call__(self, value):
        if (value.length > 200):
            raise ValidationError('Text is too long', code='invalid')
    