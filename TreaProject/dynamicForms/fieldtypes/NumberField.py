from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes import FieldFactory

from dynamicForms.statistics.NumericStatistics import NumericStatistics


class NumberField(Field.Field):
    """
    Number field type class.
    """
    template_name = "number/template.html"
    edit_template_name = "number/template_edit.html"
    prp_template_name = "number/properties.html"
    
    def check_min(self, value, min):
        if (value < min):
            raise ValidationError("Value below the minimum acceptable.")

    def check_max(self, value, max):
        if (value > max):
            raise ValidationError("Value above the maximum acceptable.")

    def validate(self, value, **kwargs):
        super(NumberField, self).validate(value, **kwargs)
        restrictions = kwargs['restrictions']
        try:
            value = int(value)
        except (ValueError, TypeError):
            raise ValidationError('Enter a valid integer.', code='invalid')
        if (restrictions['min_number']):
            self.check_min(value, restrictions['min_number'])
        if (restrictions['max_number']):
            self.check_max(value, restrictions['max_number'])
        return True

    def check_consistency(self, **kwargs):
        #When a field is created check if the restrictions are consistent
        restrictions = kwargs['restrictions']
        if (restrictions['min_number'] and restrictions['max_number']):
            if (restrictions['min_number'] > restrictions['max_number']):
                raise ValidationError("The min value might not "
                "be below the max value.")
                
    def get_statistics(self, data, field_text):
        """
        Receives a list of integers and the text associated with the field,
        returns a serialized NumericStatistics object containing statistical 
        data for the field.
        """        
        numericStatistics = NumericStatistics(data, field_text)
        return numericStatistics.getSerializedData()

    def __str__():
        return "Number"

FieldFactory.FieldFactory.register('NumberField', NumberField)