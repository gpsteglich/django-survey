from django.contrib.auth.models import User

from unittest import TestCase
from statistics import mean, pstdev
from datetime import datetime
import math
import random

from dynamicForms.statistics.StatisticsCtrl import StatisticsCtrl
from dynamicForms.statistics.NumericStatistics import NumericStatistics
from dynamicForms.statistics.ListStatistics import ListStatistics
from dynamicForms.statistics.CheckboxStatistics import CheckboxStatistics
from dynamicForms.fieldtypes.NumberField import NumberField
from dynamicForms.fieldtypes.CheckboxField import CheckboxField
from dynamicForms.fieldtypes.SelectField import SelectField
from dynamicForms.fieldtypes.TextField import TextField
from dynamicForms.models import Form, Version, FormEntry, FieldEntry





class StatisticsTestCase(TestCase):
    
    def SetUp(self):
        pass
    
    def test_NumericStatistics(self):
        
        data_list = ['1','3',"",'7','8', '4', "", '12']
        numericStatistics = NumericStatistics(data_list)

        self.assertEqual(numericStatistics.total_filled, 6, "OK")
        self.assertEqual(numericStatistics.total_not_filled, 2, "OK")
        self.assertEqual(numericStatistics.mean, round(mean([1,3,7,8,4,12]),2), "OK")
        self.assertEqual(numericStatistics.total_mean, round(mean([1,3,0,7,8,4,0,12]),2), "OK")
        self.assertEqual(numericStatistics.standard_deviation, round(pstdev([1,3,7,8,4,12]),2), "OK")
        self.assertEqual(numericStatistics.total_standard_deviation, round(pstdev([1,3,0,7,8,4,0,12]),2), "OK")
        
        numericStatistics.getSerializedData()
 
    def test_ListStatistics(self):
        
        options = [{"id": 1, "label": "Argentina"}, {"id": 2, "label": "Brasil"}, {"id": 3, "label": "Uruguay"}]
        data_list = ['1','3','3','','2','','1','2','2']
        
        listStatististcs = ListStatistics(data_list, options)
        
        self.assertEqual(listStatististcs.total_filled, 7, "OK")
        self.assertEqual(listStatististcs.total_not_filled, 2, "OK")
        self.assertListEqual(listStatististcs.total_per_option, [2,3,2], "OK")
        self.assertListEqual(listStatististcs.options, ["Argentina", "Brasil", "Uruguay"], "OK")
        
        listStatististcs.getSerializedData()
   
    def test_CheckboxStatistics(self):
        
        options = [{"id": 1, "label": "Argentina"}, {"id": 2, "label": "Brasil"}, {"id": 3, "label": "Uruguay"}]
        data_list = ["1#2","3","2#3","","1#2#3","","1", "2"]
        
        checkBoxStatistics = CheckboxStatistics(data_list, options)
        
        self.assertEqual(checkBoxStatistics.total_filled, 6, "OK")
        self.assertEqual(checkBoxStatistics.total_not_filled, 2, "OK")
        self.assertListEqual(checkBoxStatistics.total_per_option, [3,4,3], "OK")
        self.assertListEqual(checkBoxStatistics.options, ["Argentina", "Brasil", "Uruguay"], "OK")
        
        checkBoxStatistics.getSerializedData()

    def test_StatisticsCtrl(self):
        

        user = User(username='nombre',email='mail', password='password')
        user.save()
        form = Form(title="formulario 1", slug="formulario-1", owner=user)
        form.save()
        json = '{"logic": {"fields": {}, "pages": {}}, "pages": [{"fields": [{"tooltip": "", "field_type": "NumberField", "validations": {"max_number": 100, "min_number": 0}, "dependencies": {"fields": [], "pages": []}, "field_id": 1, "answer": [], "text": "Numero", "required": false}, {"tooltip": "", "field_type": "CheckboxField", "options": [{"label": "Leer", "id": 1}, {"label": "TV", "id": 2}, {"label": "Deportes", "id": 3}], "validations": {}, "dependencies": {"fields": [], "pages": []}, "max_id": 3, "field_id": 2, "answer": [], "text": "Hobbies", "required": false}, {"tooltip": "", "field_type": "SelectField", "options": [{"label": "Argentina", "id": 1}, {"label": "Uruguay", "id": 2}, {"label": "Brasil", "id": 3}], "validations": {}, "dependencies": {"fields": [], "pages": []}, "max_id": 3, "field_id": 3, "answer": [], "text": "Paises", "required": false}, {"tooltip": "", "field_type": "TextField", "validations": {"max_len_text": 255}, "dependencies": {"fields": [], "pages": []}, "field_id": 4, "answer": [], "text": "Nombre", "required": false}], "subTitle": "pagina"}], "after_submit": {"sendMail": false, "action": "Show Message", "redirect": "http://", "mailRecipient": "", "message": "Thank you. You successfully filled the form!", "mailSender": "", "mailText": "", "mailSubject": ""}}'
        version = Version(json=json, form=form)
        version.save()
        for i in range(0,12):
            entry = FormEntry(version=version)
            entry.entry_time = datetime.now()
            entry.save()
            for j in range(1,5):
                if j == 1:
                    fieldEntry = FieldEntry(field_id=j, field_type="NumberField", required=True, answer = random.randint(1, 100), entry=entry, text="Numero", shown=True)
                elif j == 2:
                    num = i % 4
                    if num == 0:
                        answer = "1#2"
                    elif num == 1:
                        answer = "1"
                    elif num == 2:
                        answer = "3"
                    else:
                        answer = "2#3"
                    fieldEntry = FieldEntry(field_id=j, field_type="CheckboxField", required=False, answer = answer, entry=entry, text="Hobbies", shown=True)
                elif j == 3:
                    fieldEntry = FieldEntry(field_id=j, field_type="SelectField", required=False, answer = str(random.randint(1, 3)), entry=entry, text="Paises", shown=True)
                else: 
                    fieldEntry = FieldEntry(field_id=j, field_type="TextField", required=False, answer = "text" + str(i), entry=entry, text="Nombre", shown=True)
                fieldEntry.save()

      
                
        
        #statistics without filter
        statistics1 = StatisticsCtrl().getStatistics(form.pk, version.number)
        
        #equal filter
        statistics2 = StatisticsCtrl().getStatistics(form.pk, version.number, "2", "equals", "1")
        form.delete()

               
                 
                    
                
        
        
        
        
        
        
        