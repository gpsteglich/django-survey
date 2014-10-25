from dynamicForms.serializers import ListStatisticsSerializer 

class ListStatistics():
    
    """
    Class with the statistics info of a number  field  
    """
    
    def __init__(self, data_list, options):
        
        self.total_per_option = []        
        self.options = options
        self.total_filled = 0
        self.total_not_filled = 0
             
        #initiate list   
        total_options = len(options)
        for i in range(0, total_options):
            self.total_per_option.append(0)
            
        #count and remove null values from data list and count not null values
        aux_list = []
        for data in data_list:
            if data != "":
                aux_list.append(data)
                self.total_filled += 1
            else:
                self.total_not_filled += 1
                 
        for data in aux_list:
            pos = 0
            while (pos != total_options) and (int(data) != options[pos]):
                pos +=1
            if pos != total_options:
                self.total_per_option[pos] += 1
            else:
                raise Exception("Data does not match with any option")
            
    def getSerializedData(self):
        return ListStatisticsSerializer(self).data
            
        