

class Renderer(object):
    """
    Default renderer
    """
    template_name = 'default'
    
    def getTemplate(self):
        return self.template_name