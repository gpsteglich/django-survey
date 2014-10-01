

class FieldRenderer(object):
    """
    Default renderer
    """
    template_name = 'default'
    
    
    def __call__(self, value):
        #default validation or pass
        return template_name