from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import json

from dynamicForms.models import Form, FieldEntry, Version, FormEntry
from dynamicForms.fields import Validations, Dependencies, Field, Option
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory

from rest_framework import serializers
import ast


class FormSerializer(serializers.ModelSerializer):
    """
    Complete serializer for the forms used for the REST framework
    """
    owner = serializers.Field(source='owner.username')
    versions = serializers.RelatedField(many=True)

    class Meta:
        model = Form
        fields = ('id', 'title', 'slug', 'versions', 'owner')
        read_only_fields = ('slug', 'id', )


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
                f_type = Factory.get_class(field['field_type'])
                kw = {}
                val = Validations()
                f = Field()
                data = FieldSerializer(f, field)
                if (data.is_valid()):
                    kw['field'] = f
                serializer = ValidationSerializer(val, field['validations'])
                if serializer.is_valid():
                    kw['restrictions'] = val
                else:
                    raise ValidationError("Validations not recognized.")
                if 'options' in field:
                    kw['options'] = field['options']
                f_type().check_consistency(**kw)
        return attrs

    class Meta:
        model = Version
        fields = ('number', 'status', 'publish_date', 'expiry_date',
                 'json', 'form')
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
        

class ValidationSerializer(serializers.Serializer):
    """
    Serializer for the validations in the versions json
    """
    max_len_text = serializers.IntegerField(required=False)
    max_number = serializers.IntegerField(required=False)
    min_number = serializers.IntegerField(required=False)
        
    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.max_len_text = attrs.get('max_len_text', instance.max_len_text)
            instance.max_number = attrs.get('max_number', instance.max_number)
            instance.min_number = attrs.get('min_number', instance.min_number)
            return instance
        return Validations(**attrs)
    

class OptionSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=100, required=False)
    id = serializers.IntegerField(required=False)
    
    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.label = attrs.get('label', instance.label)
            instance.id = attrs.get('id', instance.id)
            return instance
        else:
            opt = Option()
            opt.label = attrs.get('label', opt.label)
            opt.id = attrs.get('id')
            return opt
    

class DependencySerializer(serializers.Serializer):
    pages = serializers.CharField(required=False)
    fields = serializers.CharField(required=False)
    
    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.fields = ast.literal_eval(attrs.get('fields', instance.fields))
            instance.pages = ast.literal_eval(attrs.get('pages', instance.pages))
            return instance
        return Dependencies(**attrs)
        
class FieldSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=50)
    required = serializers.BooleanField(required=True)
    tooltip = serializers.CharField(required=False, max_length=300)
    answer = serializers.CharField(required=False)
    options = OptionSerializer(many=True, required=False, allow_add_remove=True, read_only=False)
    dependencies = DependencySerializer(required=False)
    validations = ValidationSerializer(required=False)
    max_id = serializers.IntegerField(required=False)
    field_type = serializers.CharField(required=True, max_length=30)
    field_id = serializers.IntegerField(required=True)
    

    def restore_object(self, attrs, instance=Field()):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.text = attrs.get('text', instance.text)
            instance.required = attrs.get('required', instance.required)
            instance.tooltip = attrs.get('tooltip', instance.tooltip)
            instance.answer = attrs.get('answer', instance.answer)
            instance.options = attrs.get('options', instance.options)
            #instance.dependencies = attrs.get('dependencies', instance.dependencies)
            #instance.validations = attrs.get('validations', instance.validations)
            instance.max_id = attrs.get('max_id', instance.max_id)
            instance.field_type = attrs.get('field_type', instance.field_type)
            instance.field_id = attrs.get('field_id', instance.field_id)

            return instance
        return Field(**attrs)
    

class NumericStatisticsSerializer(serializers.Serializer):  
    """
    Serializer for NumericStatistics
    """
    mean       = serializers.FloatField()
    standard_deviation = serializers.FloatField()
    total_mean  = serializers.FloatField()
    total_filled = serializers.IntegerField()
    total_not_filled = serializers.IntegerField()
    total_standard_deviation = serializers.FloatField()
    quintilesY  = serializers.CharField()
    quintilesX  = serializers.CharField()
    
class ListStatisticsSerializer(serializers.Serializer):
    """
    Serializer for ListStatistics
    """
    options          = serializers.CharField()
    total_per_option = serializers.CharField()
    total_filled     = serializers.IntegerField()
    total_not_filled = serializers.IntegerField()
    
    
