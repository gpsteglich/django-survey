from django.contrib.auth.models import User

from dynamicForms.models import Form
from rest_framework import serializers


class FormSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    class Meta:
        model = Form
        fields = ('title', 'slug', 'status', 'publish_date', 'expiry_date', 'version', 'owner', 'json')
    

class NewFormSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    
    class Meta:
        model = Form
        fields = ('title', 'owner', 'json')
        

class UserSerializer(serializers.ModelSerializer):
    forms = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'forms')
        
        
        
