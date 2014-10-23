from django.core.exceptions import ValidationError
from dynamicForms.models import Form, Version, FormEntry, FieldEntry 


class Field(object):
    """
    Default abstract field type class
    """
    folder = "fields/"
    template_name = "field_template_base.html"
    edit_template_name = "fiel_template_edit_base.html"
    prp_template_name = "field_properties_base.html" 

    def validate(self, value, **kwargs):
        #default validation or pass
        if not value:
            raise ValidationError("Problem with the answer.")
        return True

    def get_validations(self, json, id):
        for page in json['pages']:
            for field in page['fields']:
                if (field['field_id'] == id):
                    return field['validations']

    def get_options(self, json, id):
        for page in json['pages']:
            for field in page['fields']:
                if (field['field_id'] == id):
                    return field['options']

    def check_consistency(self, **kwargs):
        #When a field is created check if the restrictions are consistent
        pass

    def count_responses_pct(self, form_pk, version_num, field_id):
        v = Version.objects.get(number=version_num, form_id=form_pk)
        queryset = FieldEntry.objects.filter(field_id=field_id, entry__version_id=v.pk)
        total = queryset.count()
        responses = total - queryset.filter(answer="").count()
        return (responses, total)
    
    def get_statistics(self, data_list, options):
        """
        returns a the statistics related to the data list. 
        """
        return {}
    
    
    """
    Default Render methods for field templates
    """
    def render(self):
        return self.folder + self.template_name

    def render_properties(self):
        return self.folder + self.prp_template_name
    
    def render_edit(self):
        return self.folder + self.edit_template_name
    
    def render_statistic(self):
        return self.folder + self.sts_template_name
    
    class Meta:
        abstract = True
