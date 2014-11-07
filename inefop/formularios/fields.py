from django.core.exceptions import ValidationError
import re

from dynamicForms.fieldtypes import Field
from dynamicForms.fieldtypes import ModelField
from dynamicForms.fieldtypes import FieldFactory
from formularios.models import Usuario, Club


class UsuarioField(ModelField.ModelField):
    prp_template_name = "usuario/properties.html"
    model = Usuario
    name =  "Usuario"

    def get_assets():
        return ['formularios/js/fields/Usuario.js']
    
    def __str__(self):
        return "Usuario"
    
FieldFactory.FieldFactory.register('UsuarioField', UsuarioField)


class ClubField(ModelField.ModelField):
    prp_template_name = "club/properties.html"
    model = Club
    name =  "Club"
    
    def get_assets():
        return ['formularios/js/fields/Club.js']
    
    def __str__(self):
        return "Club"
    
FieldFactory.FieldFactory.register('ClubField', ClubField)


class MatriculaField(Field.Field):
    template_name = "matricula/template.html"
    edit_template_name = "matricula/template_edit.html"
    prp_template_name = "matricula/properties.html"
    digits = 4
    letters = 3
    
    def pattern_check(self, value, **kwargs):
        regex = r"[A-Z]{" + self.letters.__str__() + "}[0-9]{" + \
            self.digits.__str__() + "}"
        result = re.match(regex, value);
        if (result == None):
            raise ValidationError("Not a valid format.")
        
    def get_methods(self, **kwargs):
        #default validation or pass
        base = super(MatriculaField, self).get_methods(**kwargs)
        base.append(self.pattern_check)
        return base

    def get_assets():
        return ['formularios/js/fields/Matricula.js']
    
    def __str__(self):
        return "Matricula"
    
FieldFactory.FieldFactory.register('MatriculaField', MatriculaField)
