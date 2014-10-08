from dynamicForms.fieldtypes.Field import Field
from dynamicForms.fieldtypes import FieldFactory

class CheckboxField(Field):
    """
    Checkbox field validator, render and analize methods
    """
    

    """
    Render methods for TextField template
    """
    def render(self):
        return 'fields/checkbox/template.html'

    def render_properties(self):
        return 'fields/checkbox/properties.html'

    def __str__():
        return "Checkbox"
    
    
FieldFactory.FieldFactory.register('CheckboxField', CheckboxField)