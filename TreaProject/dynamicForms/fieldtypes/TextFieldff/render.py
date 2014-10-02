
from dynamicForms.fieldtypes.Field import render

class Renderer(render.Renderer):
    """
    Text field renderer
    """
    template_name = "question_char.html"       
    
    def getTemplate(self):
        #default validation or pass
        return super(Renderer,self).getTemplate(self)