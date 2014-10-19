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

    def get_options(self, json, id):
        for page in json['pages']:
            for field in page['fields']:
                if (field['field_id'] == id):
                    return field['options']


    class Meta:
        abstract = True