from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes import FieldFactory

class TextField(Field.Field):
    """
    Text field validator, render and analize methods
    """
    def check_length(self, value, length):
            if (len(value) > length):
                raise ValidationError("Text is too long")
            
    def validate(self, value, restrictions):
        super(TextField,self).validate(value,restrictions)
        if (restrictions['max_len_text']):
            self.check_length(value, restrictions['max_len_text'])
        return True
    
    def check_consistency(self, restrictions):
        #When a field is created check if the restrictions are consistent
        if (restrictions['max_len_text']):
            if (restrictions['max_len_text'] < 0):
                raise ValidationError("Max length might not be less than 0.")


    """
    Render methods for TextField template
    """
    def render(self):
        return 'fields/text/template.html'

    def render_properties(self):
        return 'fields/text/properties.html'

    def __str__():
        return "Single Line Text"
    
    
FieldFactory.FieldFactory.register('TextField', TextField)
    