from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.ListField import ListField
from dynamicForms.fieldtypes import FieldFactory
from dynamicForms.statistics.CheckboxStatistics import CheckboxStatistics


class CheckboxField(ListField):
    """
    Checkbox field validator, render and analize methods
    """
    template_name = "checkbox/template.html"
    edit_template_name = "checkbox/template_edit.html"
    prp_template_name = "checkbox/properties.html"
    sts_template_name = "checkbox/template_statistic.html"

                    
    def get_statistics(self, data_list, field):
        checkboxStatistics = CheckboxStatistics(data_list, field["options"])
        statistics = checkboxStatistics.getSerializedData()
        statistics["field_text"] = field["text"] 
        if field["required"]:
            statistics["required"] = "Yes"
        else:
            statistics["required"] = "No"
        return statistics
      

    def belong_check(self, value, **kwargs):
        field = kwargs['field']
        top = field.max_id
        for v in value.split('#'):
            v = int(v)
            if not (v > 0 and v <= top):
                raise ValidationError("Invalid value, not among options.")

    def __str__(self):
        return "Checkbox"


FieldFactory.FieldFactory.register('CheckboxField', CheckboxField)
