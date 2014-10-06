from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import Field

class Validator(Field.Validator):
    """
    Default validator
    """
    def check_length(self, value, length):
            if (len(value) > length):
                raise ValidationError("Text is too long")
            
    def validate(self, value, restrictions):
        #default validation or pass
        super(Validator,self).validate(value,restrictions)
        if (restrictions['max_len_text']):
            self.check_length(value, restrictions['max_len_text'])
        return True
    
    def check_consistency(self, restrictions):
        #When a field is created check if the restrictions are consistent
        if (restrictions['max_len_text']):
            if (restrictions['max_len_text'] < 0):
                raise ValidationError("Max length might not be less than 0.")


class Renderer(Field.Renderer):
    """
    Renderer for TextAreaField template
    """
    def render_type(self):
        return 'fields/text_area/template.html'

    def render_properties(self):
        return 'fields/text_area/properties.html'