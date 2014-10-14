from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from dynamicForms.fieldtypes import TextField
from dynamicForms.fieldtypes import FieldFactory


class EmailField(TextField.TextField):
    """
    Email validator using django's validation
    """

    def validate(self, value, **kwargs):
        super(EmailField, self).validate(value, **kwargs)
        try:
            validate_email(value)
        except ValidationError as e:
            #transform the message to be cathed later.
            raise ValidationError(e.__str__())

    """
    Render methods for EmailField template
    """
    def render(self):
        return 'fields/email/template.html'

    def render_properties(self):
        return 'fields/email/properties.html'

    def __str__():
        return "Email"

FieldFactory.FieldFactory.register('EmailField', EmailField)