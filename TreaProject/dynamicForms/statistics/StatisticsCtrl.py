from dynamicForms.models import Form, Version, FieldEntry
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
import json


class StatisticsCtrl():
    

    def getStatistics(self, formId, versionNum):
        """
         Receives a the id of a version (formId, versionNum),
         returns the statistics of each field on it
        """

        form = Form.objects.get(pk=formId)
        version = form.versions.get(number=versionNum)
        
        loaded = json.loads(version.json)
        pages = loaded["pages"]
   
        statistics = {}
        for page in pages:
            nro = 1
            for field in page["fields"]:
                fieldEntries = FieldEntry.objects.filter(field_id=field["field_id"], entry__version_id=version.pk) 
                if len(fieldEntries) != 0:
                    data = []
                    for fieldEntry in fieldEntries:
                        data.append(fieldEntry.answer)                                      
                    fieldType = Factory.get_class(field["field_type"])
                    fieldStatistics = fieldType().get_statistics(data, field["options"])
                    fieldStatistics["field_type"] = field["field_type"]
                    fieldStatistics["field_text"] = field["text"]
                    statistics[field["field_id"]] = fieldStatistics
                else:
                    raise Exception("There are no field entries for this form.")
                
        return statistics
                
                    
                    
                
        
        
        
        
            
        
     
        
       
