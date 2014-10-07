from django.core.exceptions import Exception


class FieldFactory():
    #factory

    fields = {}
    

    def get_class(id):
        return fields[id] 
    
    def register(id, type):
        if not fields[id]:
            fields[id] = type
        else:
            raise Exception("invalid ID.")
       
    