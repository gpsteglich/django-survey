from django.core.exceptions import ValidationError
import re

from dynamicForms.fieldtypes import Field
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
    
    def __str__(self):
        return "Usuario"
    
FieldFactory.FieldFactory.register('UsuarioField', UsuarioField)

class MatriculaField(Field.Field):
    template_name = "matricula/template.html"
    edit_template_name = "matricula/template_edit.html"
    prp_template_name = "matricula/properties.html"
    digits = 4
    letters = 3
    
    def pattern_check(self, value, **kwargs):
        regex = r"[A-Z]{" + re.escape("%d", letters) + "}[0-9]{" + \
            re.escape("%d", digits) + "}"
        result = re.match(regex, value);
        if (result == None):
            raise ValidationError("Not a valid format.")
        
    def get_methods(self, **kwargs):
        #default validation or pass
        base = super(MatriculaField, self).get_methods(**kwargs)
        base.append(self.pattern_check)
        return base
    
    def __str__(self):
        return "Matricula"
    
FieldFactory.FieldFactory.register('MatriculaField', MatriculaField)