# tests/test_nicecharts.py
import os
import pytest
from nicecharts import fan_chart, line_chart, pie_chart

def test_fan_chart_svg():
    outfile = "test_fan.svg"
    fan_chart(values=[30, 20, 50], labels=["A","B","C"], title="Fan Test", outfile=outfile)
    assert os.path.exists(outfile)
    os.remove(outfile)

def test_fan_chart_png():
    outfile = "test_fan.png"
    fan_chart(values=[30, 20, 50], labels=["A","B","C"], title="Fan Test", outfile=outfile)
    assert os.path.exists(outfile)
    os.remove(outfile)

def test_line_chart():
    outfile = "test_line.svg"
    line_chart(x=[1,2,3], y=[10,20,15], title="Line Test", outfile=outfile)
    assert os.path.exists(outfile)
    os.remove(outfile)

def test_pie_chart():
    outfile = "test_pie.svg"
    pie_chart(values=[40,60], labels=["X","Y"], title="Pie Test", outfile=outfile)
    assert os.path.exists(outfile)
    os.remove(outfile)