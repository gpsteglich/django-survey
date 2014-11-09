from dynamicForms.models import Form, Version, FieldEntry
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
import json


class StatisticsCtrl():
    

    def getStatistics(self, formId, versionNum, fieldId=None, filterType=None, filter=None):
        """
         Receives a the id of a version (formId, versionNum),
         returns the statistics of each field on it
        """

        form = Form.objects.get(pk=formId)
        version = form.versions.get(number=versionNum)

        if filterType == "equals":
            fieldEntries = Version.objects.get_entries(version.pk).data_iexact(field_id=fieldId, data=filter).get_data()
        elif filterType == "contains":
            fieldEntries = Version.objects.get_entries(version.pk).data_icontains(field_id=fieldId, data=filter).get_data()
        else:
            fieldEntries = Version.objects.get_entries(version.pk).get_data()
        
        if fieldEntries:

            loaded = json.loads(version.json)
            pages = loaded["pages"]

            statistics = {}
            for page in pages:
                for field in page["fields"]:
                    data = []
                    for fieldEntry in fieldEntries:
                        if fieldEntry.field_id == field["field_id"]:
                            data.append(fieldEntry.answer)                                      
                    fieldType = Factory.get_class(field["field_type"])
                    fieldStatistics = fieldType().get_statistics(data, field)
                    statistics[field["field_id"]] = fieldStatistics
        else:
            raise Exception("There are no field entries for this form.")
            
     
        return statistics
                
                    
                    
                
        
        
        
        
            
        
     
        
       
