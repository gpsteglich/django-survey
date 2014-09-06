from rest_framework import serializers
from django.contrib.auth.models import User

from dynamicForms.models import Form

class FormSerializer(serializers.ModelSerializer):
    
    user = serializers.Field(source='user.username')
    class Meta:
        model = Form
        fields = ('title', 'slug', 'status', 'publish_date', 'expiry_date', 'version', 'owner', 'json')
    

class UserSerializer(serializers.ModelSerializer):
    forms = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'forms')
        
        
        