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
    
    def check_length(self, value, **kwargs):
        val = kwargs['restrictions']
        if (len(value) > val.max_len_text):
            raise ValidationError("Text is too long")

    def get_methods(self, **kwargs):
        #default validation or pass
        base = super(TextField, self).get_methods(**kwargs)
        val = kwargs['restrictions']
        if (val.max_len_text != None):
            base.append(self.check_length)
        return base

    def check_consistency(self, field):
        #When a field is created check if the restrictions are consistent
        val = field.validations
        if (not val.valid_text()):
            raise ValidationError("Max length might not be less than 0.")

    def __str__(self):
        return "Single Line Text"


FieldFactory.FieldFactory.register('TextField', TextField)
