from dynamicForms.serializers import ListStatisticsSerializer

class CheckboxStatistics():
    
    def __init__(self, data_list, options):
        
        self.total_per_option = []        
        self.options = options
        self.total_filled = 0
        self.total_not_filled = 0
        
        #initiate list   
        total_options = len(options)
        for i in range(0, total_options):
            self.total_per_option.append(0)
            
        #count and remove null values
        #count not null values data and insert them into an auxiliary list
        aux_list = []
        for data in data_list:
            if data != "":
                aux_list += data.split("#")
                self.total_filled += 1
            else:
                self.total_not_filled += 1
                 
        for data in aux_list:
            pos = 0
            while (pos != total_options) and (data != options[pos]):
                pos +=1
            if pos != total_options:
                self.total_per_option[pos] += 1
            else:
                raise Exception("Data does not match with any option")
            
    def getSerializedData(self):
        return ListStatisticsSerializer(self).data