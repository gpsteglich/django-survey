from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import TextField
from dynamicForms.fieldtypes import FieldFactory

class TextAreaField(TextField.TextField):
    """
    Validator for text area is the same as simple TextField
    """

    def validate(self, value, restrictions):
        super(TextAreaField,self).validate(value,restrictions)

    """
    Render methods for TextAreaField template
    """
    def render_type(self):
        return 'fields/text_area/template.html'

    def render_properties(self):
        return 'fields/text_area/properties.html'
    
    def __str__():
        return "Multi Line Text"
    
FieldFactory.FieldFactory.register('TextAreaField', TextAreaField)