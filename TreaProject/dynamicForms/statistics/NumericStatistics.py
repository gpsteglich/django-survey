from statistics import mean, pstdev
import math

from dynamicForms.statistics.serializers import NumericStatisticsSerializer 

class NumericStatistics():
    
    """
    Class with the statistics info of a number  field  
    """
    
    def __init__(self, data_list):
           
        
        listTotal = []    #null values are counted as 0
        list = []         #without null values
        self.total_filled = 0
        self.total_not_filled = 0
        for data in data_list:
            if data != "":
                listTotal.append(int(data))
                list.append(int(data))
                self.total_filled += 1 
            else:
                listTotal.append(0)
                self.total_not_filled += 1
           
        self.mean       = round(mean(list), 2)
        self.standard_deviation = round(pstdev(list, self.mean), 2)
        self.total_mean = round(mean(listTotal), 2)
        self.total_standard_deviation = round(pstdev(listTotal, self.total_mean), 2)
        self.quintilesX  = []
        self.quintilesY = []
        
        minimum  = min(list)
        maximum  = max(list)

        quintile_length  = math.floor((maximum - minimum + 1) /5)
        
        #first 4 quintiles
        first = minimum
        for i in range(1, 5):
            second = first + quintile_length
            quintileX = "[" + str(first) + ", " + str(second) + ")" 
            self.quintilesX.append(quintileX)
            quintileY = 0
            for num in list:
                if (first <= num) and (num < second):
                    quintileY += 1
            self.quintilesY.append(quintileY)
            first = second
            
        #last quintile
        self.quintilesX.append("[" + str(first) + ", " + str(maximum) + "]")
        quintileY = 0
        for num in list:
            if (first <= num) and (num <= maximum):
                quintileY += 1
        self.quintilesY.append(quintileY)
        
        
    def getSerializedData(self):
        return NumericStatisticsSerializer(self).data
        
        
            
            
            
    
    
    
