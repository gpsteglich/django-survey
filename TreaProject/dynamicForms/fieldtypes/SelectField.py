from dynamicForms.fieldtypes.Field import Field
from dynamicForms.fieldtypes import FieldFactory

class SelectField(Field):
    """
    Combobox field validator, render and analize methods
    """
    

    """
    Render methods for TextField template
    """
    def render(self):
        return 'fields/combobox/template.html'

    def render_properties(self):
        return 'fields/combobox/properties.html'

    def __str__():
        return "Combo Box"
    
    
FieldFactory.FieldFactory.register('SelectField', SelectField)