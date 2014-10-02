from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import Field

class Validator(Field.Validator):
    """
    Default validator
    """
    def check_min(self, value, min):
        if (value < min):
            raise ValidationError("Value below the minimum acceptable.")        
      
    def check_max(self, value, max):
        if (value > max):
            raise ValidationError("Value above the maximum acceptable.") 
              
    def validate(self, value, restrictions):
        #default validation or pass
        super(Validator,self).validate(value,restrictions)
        try:
            int(value)
        except (ValueError, TypeError):
            raise ValidationError('Enter a valid integer.', code='invalid')
        if (restrictions['min_number']):
            self.check_min(value, restrictions['min_number'])
        if (restrictions['max_number']):
            self.check_max(value, restrictions['max_number'])    
        return True