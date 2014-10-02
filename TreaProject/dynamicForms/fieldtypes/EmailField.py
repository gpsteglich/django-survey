from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from dynamicForms.fieldtypes import Field

class Validator(Field.Validator):
    """
    Default validator
    """

    def validate(self, value, restrictions):
        #default validation or pass
        validate_email(value)