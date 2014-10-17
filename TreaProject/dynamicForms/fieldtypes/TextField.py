from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes import FieldFactory


class TextField(Field.Field):
    """
    Text field validator, render and analize methods
    """
    template_name = "text/template.html"
    edit_template_name = "text/template_edit.html"
    prp_template_name = "text/properties.html"
    
    def check_length(self, value, length):
            if (len(value) > length):
                raise ValidationError("Text is too long")

    def validate(self, value, **kwargs):
        super(TextField, self).validate(value, **kwargs)
        restrictions = kwargs['restrictions']
        if (restrictions['max_len_text']):
            self.check_length(value, restrictions['max_len_text'])
        return True

    def check_consistency(self, **kwargs):
        #When a field is created check if the restrictions are consistent
        restrictions = kwargs['restrictions']
        if (restrictions['max_len_text']):
            if (restrictions['max_len_text'] < 0):
                raise ValidationError("Max length might not be less than 0.")

    def __str__():
        return "Single Line Text"


FieldFactory.FieldFactory.register('TextField', TextField)
