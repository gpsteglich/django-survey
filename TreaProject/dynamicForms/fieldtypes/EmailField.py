from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from dynamicForms.fieldtypes import TextField
from dynamicForms.fieldtypes import FieldFactory


class EmailField(TextField.TextField):
    """
    Email validator using django's validation
    """
    template_name = "email/template.html"
    edit_template_name = "email/template_edit.html"
    prp_template_name = "email/properties.html"
    
    def validate(self, value, **kwargs):
        super(EmailField, self).validate(value, **kwargs)
        try:
            validate_email(value)
        except ValidationError as e:
            #transform the message to be cathed later.
            raise ValidationError(e.__str__())

    def __str__():
        return "Email"

FieldFactory.FieldFactory.register('EmailField', EmailField)