from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.Field import Field


class ListField(Field):
    """
    List field validator, render and analize methods
    """
    
    def check_consistency(self, **kwargs):
        options = kwargs['options']
        if (options == []):
            raise ValidationError("List fields need at least one option.")
       
    class Meta:
        abstract = True