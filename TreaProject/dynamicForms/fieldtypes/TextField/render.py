
from dynamicForms.fieldtypes.Field import render

class TextFieldRenderer(render.FieldRenderer):
    """
    Text field renderer
    """
    
    def __call__(self):
        #default validation or pass
        template_name = 'default'
        return super(FieldRenderer,self)