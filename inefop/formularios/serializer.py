
from rest_framework import serializers
from formularios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('name', 'surname', 'birthdate', 'has_car')