from nicecharts import fan_chart, line_chart, pie_chart
import os

# Tạo folder output
output_dir = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(output_dir, exist_ok=True)


fan_chart([30,50,20], outfile=os.path.join(output_dir, "fan_chart.svg"))
line_chart([1,2,3,4], [10,20,15,25], outfile=os.path.join(output_dir, "line_chart.svg"))
pie_chart([10,20,30,40], outfile=os.path.join(output_dir, "pie_chart.svg"))

