from django.contrib.auth.models import User
import json

from dynamicForms.models import Form, FieldEntry, Version, FormEntry
from dynamicForms.fieldtypes.field_type import FIELD_FILES

from rest_framework import serializers


class FormSerializer(serializers.ModelSerializer):
    """
    Complete serializer for the forms used for the REST framework
    """
    owner = serializers.Field(source='owner.username')
    versions = serializers.RelatedField(many=True)
    
    class Meta:
        model = Form
        fields = ('id', 'title', 'slug', 'versions', 'owner')
        read_only_fields = ('slug','id',)


class VersionSerializer(serializers.ModelSerializer):
    """
    Complete serializer for the forms used for the REST framework
    """
    form = serializers.Field(source='form.title')
    json = serializers.CharField(required=False)
    
    def validate_json(self, attrs, source):
        value = json.loads(attrs[source])
        for page in value['pages']:
            for field in page['fields']:
                file = FIELD_FILES[int(field['field_type'])]
                field_validator = __import__( file , fromlist=["Validator"])
                x = field_validator.Validator()
                x.check_consistency(field['validations'])
        return attrs
        
        
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

class FormEntrySerializer(serializers.ModelSerializer):
    """
    Serializer for the form entries
    """
    fields = serializers.RelatedField(many=True)
    
    class Meta:
        model = FormEntry
        fields = ('entry_time', 'fields')
        
        