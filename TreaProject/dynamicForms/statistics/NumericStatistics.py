from statistics import mean, pstdev
import math

from dynamicForms.serializers import NumericStatisticsSerializer 

class NumericStatistics():
    
    """
    Class with the statistics info of a number  field  
    """
    
    def __init__(self, data_list, field_text):
           
        
        list = []
        for data in data_list:
            if data != "":
                list.append(int(data))
            else:
                list.append(0)
           
        self.field_text = field_text
        self.mean       = mean(list)
        self.standard_deviation = pstdev(list, self.mean)
        self.quintilesX  = []
        self.quintilesY = []
        
        minimum  = min(list)
        maximum  = max(list)

        quintile_length  = math.ceil((maximum - minimum + 1) /5)
        
        #first 4 quintiles
        first = minimum
        for i in range(1, 5):
            second = first + quintile_length
            quintileX = "Between " + str(first) + " and " + str(second) 
            self.quintilesX.append(quintileX)
            quintileY = 0
            for num in list:
                if (first <= num) and (num < second):
                    quintileY += 1
            self.quintilesY.append(quintileY)
            first = second
            
        #last quintile
        self.quintilesX.append("Between " + str(first) + " and " + str(maximum))
        quintileY = 0
        for num in list:
            if (first <= num) and (num <= maximum):
                quintileY += 1
        self.quintilesY.append(quintileY)
        
        
    def getSerializedData(self):
        return NumericStatisticsSerializer(self).data
        
        
            
            
            
    
    
    