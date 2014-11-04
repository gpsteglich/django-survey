
from rest_framework import serializers
from formularios.models import Usuario, Club, Country

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('name', 'surname', 'birthdate', 'has_car')
        
        
class ClubSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Club
        fields = ('name', 'established', 'country')
        

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ('name',)