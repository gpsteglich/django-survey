from statistics import mean, pstdev
import math

from dynamicForms.serializers import NumericStatisticsSerializer 

class NumericStatistics():
    
    """
    Class with the statistics info of a number  field  
    """
    
    def __init__(self, data_list):
           
        
        listTotal = []    #null values are counted as 0
        list = []         #without null values
        for data in data_list:
            if data != "":
                listTotal.append(int(data))
                list.append(int(data))
            else:
                listTotal.append(0)
           
        self.mean       = mean(list)
        self.standard_deviation = pstdev(list, self.mean)
        self.total_mean = mean(listTotal)
        self.total_standard_deviation = pstdev(listTotal, self.total_mean)
        self.quintilesX  = []
        self.quintilesY = []
        
        minimum  = min(list)
        maximum  = max(list)

        quintile_length  = math.floor((maximum - minimum + 1) /5)
        
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
        
        
            
            
            
    
    
    