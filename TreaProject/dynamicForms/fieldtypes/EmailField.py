from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from dynamicForms.fieldtypes import Field

class Validator(Field.Validator):
    """
    Default validator
    """

    def validate(self, value, restrictions):
        #default validation or pass
        try:
            validate_email(value)
        except ValidationError as e:
            raise ValidationError(e.__str__())


class Renderer(Field.Renderer):
    """
    Renderer for EmailField template
    """
    def render(self):
        return 'fields/email/template.html'

    def render_properties(self):
        return 'fields/email/properties.html'