from django.core.exceptions import ValidationError

class Field(object):
    """
    Default abstract field type class
    """
    
    def validate(self, value, **kwargs):
        #default validation or pass
        if not value:
            raise ValidationError("Problem with the answer.")
        return True
    
    def get_validations(self, json, id):
        for page in json['pages']:
            for field in page['fields']:
                if (field['field_id'] == id):
                    return field['validations']
                
    def get_options(self, json, id):
        for page in json['pages']:
            for field in page['fields']:
                if (field['field_id'] == id):
                    return field['options']
                
    def check_consistency(self, **kwargs):
        #When a field is created check if the restrictions are consistent
        pass
    
    """
    Default Render methods for field templates
    """
    def render(self):
        pass

    def render_properties(self):
        pass
    
    class Meta:
        abstract = True
