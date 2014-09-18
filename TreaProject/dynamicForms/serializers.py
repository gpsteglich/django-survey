from django.contrib.auth.models import User

from dynamicForms.models import Form, FieldEntry, Version
from rest_framework import serializers


class FormSerializer(serializers.ModelSerializer):
    """
    Complete serializer for the forms used for the REST framework
    """
    owner = serializers.Field(source='owner.username')
    versions = serializers.RelatedField(many=True)
    
    class Meta:
        model = Form
        fields = ('title', 'slug', 'versions', 'owner')
        read_only_fields = ('slug',)


class VersionSerializer(serializers.ModelSerializer):
    """
    Complete serializer for the forms used for the REST framework
    """
    owner = serializers.Field(source='form.title')
    json = serializers.CharField(required=False)
    
    class Meta:
        model = Version
        fields = ('number', 'status', 'publish_date', 'expiry_date', 'json', 'form')
        read_only_fields = ('number',)
    

class UserSerializer(serializers.ModelSerializer):
    forms = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'forms')


class FieldEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FieldEntry
        fields = ('field_id', 'field_type', 'text', 'required', 'answer')

