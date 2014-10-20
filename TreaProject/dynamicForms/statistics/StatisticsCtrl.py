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
                data = []
                for fieldEntry in fieldEntries:
                    data.append(fieldEntry.answer)
                print(field["field_type"])
                fieldType = Factory.get_class(field["field_type"])
                fieldStatistics = fieldType().get_statistics(data, field["text"])
                fieldStatistics["field_type"] = field["field_type"]
                statistics[field["field_id"]] = fieldStatistics
                
        return statistics
                
                    
                    
                
        
        
        
        
            
        
     
        
       
