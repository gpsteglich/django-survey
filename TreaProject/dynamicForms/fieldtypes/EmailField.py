from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from dynamicForms.fieldtypes import TextField

class Validator(TextField.Validator):
    """
    Email validator using django's validation
    """

    def validate(self, value, restrictions):
        super(Validator,self).validate(value,restrictions)
        try:
            validate_email(value)
        except ValidationError as e:
            #transform the message to be cathed later.
            raise ValidationError(e.__str__())


class Renderer(Field.Renderer):
    """
    Renderer for EmailField template
    """
    def render(self):
        return 'fields/email/template.html'

    def render_properties(self):
        return 'fields/email/properties.html'