from django.contrib.auth.models import User

from dynamicForms.models import Form, FieldEntry
from rest_framework import serializers


class FormSerializer(serializers.ModelSerializer):
    """
    Complete serializer for the forms used for the REST framework
    """
    owner = serializers.Field(source='owner.username')
    json = serializers.CharField(required=False)
    
    class Meta:
        model = Form
        fields = ('title', 'slug', 'status', 'publish_date', 'expiry_date', 'version', 'owner', 'json')
        read_only_fields = ('slug',)


class NewFormSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    json = serializers.CharField(required=False)
    class Meta:
        model = Form
        fields = ('title' ,'owner', 'json')
        

class UserSerializer(serializers.ModelSerializer):
    forms = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'forms')


class FieldEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FieldEntry
        fields = ('field_id', 'field_type', 'text', 'required', 'answer')

