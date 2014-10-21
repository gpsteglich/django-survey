from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes import NumberField
from dynamicForms.fieldtypes import FieldFactory
from formularios.models import Usuario

class UsuarioField(NumberField.NumberField):
    template_name = "inefop/template.html"
    edit_template_name = "inefop/template_edit.html"
    prp_template_name = "inefop/properties.html"
    
    def model_check(self, value, **kwargs):
        value = int(value)
        try:
            u = Usuario.objects.get(pk=value)
        except Usuario.DoesNotExist:
            raise ValidationError("There is no such user.")
        
    def get_methods(self, **kwargs):
        #default validation or pass
        base = super(UsuarioField, self).get_methods(**kwargs)
        base.append(self.model_check)
        return base
    
    def __str__():
        return "Usuario"
    
FieldFactory.FieldFactory.register('UsuarioField', UsuarioField)