from dynamicForms.serializers import ListStatisticsSerializer 

class ListStatistics():
    
    """
    Class with the statistics info of a number  field  
    """
    
    def __init__(self, data_list, options):
        
        self.total_per_option = []        
        self.options = options
             
        #initiate list   
        total_options = len(options)
        for i in range(0, total_options):
            self.total_per_option.append(0)
                 
        for data in data_list:
            pos = 0
            while data != options[pos]:
                pos +=1
            self.total_per_option[pos] += 1
            
    def getSerializedData(self):
        return ListStatisticsSerializer(self).data
            
        