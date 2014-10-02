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
    
    