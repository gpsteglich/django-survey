from django.core.exceptions import ValidationError
import re

from dynamicForms.fieldtypes import Field

class Validator(Field.Validator):
    """
    Default validator
    """
    def check_id(self, value):
        digits = [int(i) for i in value]
        # If value has less than 8 digits, we complete with zeros on the left
        if len(digits) < 8:
            diff = 8 - len(digits)
            for x in range(0, diff + 1):
                digits.insert(0, 0)
        
        const = [2, 9, 8, 7, 6, 3, 4]
        value = 0
        for x in range(0,7):
            value += digits[x] * const[x]
        m = value % 10
        if ((10 - m) % 10) != digits[len(digits) - 1]:
            raise ValidationError('Enter a valid ID.', code='invalid')
            
    def validate(self, value, restrictions):
        #default validation or pass
        super(Validator,self).validate(value,restrictions)
        intvalue = re.sub('[.-]', '', value)
        try:
            int(intvalue)
        except (ValueError, TypeError):
            raise ValidationError('Enter a valid integer.', code='invalid')
        self.check_id(value)
        return True