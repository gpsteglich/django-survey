from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes import FieldFactory


class NumberField(Field.Field):
    """
    Number field type class.
    """
    template_name = "number/template.html"
    edit_template_name = "number/template_edit.html"
    prp_template_name = "number/properties.html"
    
    def check_min(self, value, **kwargs):
        val = kwargs['restrictions']
        if (int(value) < val.min_number):
            raise ValidationError("Value below the minimum acceptable.")

    def check_max(self, value, **kwargs):
        val = kwargs['restrictions']
        if (int(value) > val.max_number):
            raise ValidationError("Value above the maximum acceptable.")

    def int_check(self, value, **kwargs):
        try:
            int(value)
        except (ValueError, TypeError):
            raise ValidationError('Enter a valid integer.', code='invalid')
        
    def get_methods(self, **kwargs):
        #default validation or pass
        base = super(NumberField, self).get_methods(**kwargs)
        base.append(self.int_check)
        restrictions = kwargs['restrictions']
        if (restrictions.min_number != None):
            base.append(self.check_min)
        if (restrictions.max_number != None):
            base.append(self.check_max)
        return base
    
    def check_consistency(self, **kwargs):
        #When a field is created check if the restrictions are consistent
        val = kwargs['restrictions']
        if not val.valid_number():
            raise ValidationError("The min value might not "
                "be below the max value.")

    def __str__():
        return "Number"

FieldFactory.FieldFactory.register('NumberField', NumberField)