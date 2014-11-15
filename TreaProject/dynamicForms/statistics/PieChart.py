from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing 

class PieChart(Drawing):
    
    def __init__(self, data, labels):
        
        super(PieChart, self).__init__(400,200)
         
        pieChart = Pie()
        pieChart.x = 40
        pieChart.y = 30
        pieChart.width = 120
        pieChart.height = 120
        pieChart.slices.strokeWidth=0.5
        pieChart.data = data
        pieChart.labels = []
        for d in data:
            pieChart.labels.append(str(d))
            
        self.add(pieChart, "pie chart")
        
        legend = Legend()