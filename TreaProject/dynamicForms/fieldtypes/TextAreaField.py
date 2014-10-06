from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import TextField

class Validator(TextField.Validator):
    """
    Validator for text area is the same as simple TextField
    """

    def validate(self, value, restrictions):
        super(Validator,self).validate(value,restrictions)

class Renderer(TextField.Renderer):
    """
    Renderer for TextAreaField template
    """
    def render_type(self):
        return 'fields/text_area/template.html'

    def render_properties(self):
        return 'fields/text_area/properties.html'