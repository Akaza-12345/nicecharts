# 6. nicecharts/pie.py
from .fan import fan_chart

def pie_chart(values, labels=None, colors=None, title=None, outfile="pie.svg",
              width=600, height=400):
    # Pie chart is just a full circle fan chart
    fan_chart(values, labels, colors, title, outfile, width, height, full_circle=True)
