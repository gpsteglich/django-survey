from django.core.exceptions import ValidationError

from dynamicForms.fieldtypes.Field import Field
from dynamicForms.statistics.ListStatistics import ListStatistics

class ListField(Field):
    """
    List field validator, render and analize methods
    """
    
    def check_consistency(self, **kwargs):
        options = kwargs['options']
        if (options == []):
            raise ValidationError("List fields need at least one option.")
    
    def get_statistics(self, data_list, options):
        listStatistics = ListStatistics(data_list,options)
        return listStatistics.getSerializedData()
       
    class Meta:
        abstract = True