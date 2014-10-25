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
                    
    def get_statistics(self, data_list, options):
        checkboxStatistics = CheckboxStatistics(data_list, options)
        return checkboxStatistics.getSerializedData()

    def __str__(self):
        return "Checkbox"


FieldFactory.FieldFactory.register('CheckboxField', CheckboxField)