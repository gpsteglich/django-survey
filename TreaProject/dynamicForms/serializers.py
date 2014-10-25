from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import json

from dynamicForms.models import Form, FieldEntry, Version, FormEntry
from dynamicForms.fields import Validations
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory

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
        

class ValidationSerializer(serializers.ModelSerializer):
    """
    Serializer for the validations in the versions json
    """
    class Meta:
        model = Validations
        fields = ('max_len_text', 'min_number', 'max_number')

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
    