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
            value = int(value)
        except (ValueError, TypeError):
            raise ValidationError('Enter a valid integer.', code='invalid')
        if (restrictions['min_number']):
            self.check_min(value, restrictions['min_number'])
        if (restrictions['max_number']):
            self.check_max(value, restrictions['max_number'])    
        return True
    
    def check_consistency(self, restrictions):
        #When a field is created check if the restrictions are consistent
        if (restrictions['min_number'] and restrictions['max_number']):
            if (restrictions['min_number'] > restrictions['max_number']):
                raise ValidationError("The min value might not be below the max value.")
            
            
            