from django.core.exceptions import ValidationError

class Validator(object):
    """
    Default validator
    """
    def validate(self, value, restrictions):
        #default validation or pass
        if not value:
            raise ValidationError("Problem with the answer.")
        return True
    
    def get_validations(self, json, id):
        for page in json['pages']:
            for field in page['fields']:
                if (field['field_id'] == id):
                    return field['validations']
                
    def check_consistency(self, restrictions):
        #When a field is created check if the restrictions are consistent
        pass
    
    class Meta:
        abstract = True


class Renderer(object):
    """
    Default Renderer method for field templates
    """
    def render(self):
        pass

    def render_properties(self):
        pass