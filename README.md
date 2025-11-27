# README.md
# NiceCharts v1.0

**NiceCharts** là thư viện Python đơn giản giúp bạn tạo các loại biểu đồ: fan chart, line chart, và pie chart, xuất ra định dạng SVG hoặc PNG.

## 🔹 Tính năng
- Tạo **Fan Chart** (180° hoặc 360° – Pie chart)
- Tạo **Line Chart** với các điểm, nhãn trục, tiêu đề
- Xuất trực tiếp ra **SVG** hoặc **PNG**
- Màu sắc và nhãn tùy chỉnh
- Module nhẹ, dễ sử dụng, không phụ thuộc matplotlib

## 🔹 Cài đặt
```bash
pip install Pillow cairosvg
# Hoặc sau khi upload PyPI:
pip install nicecharts
```

## 🔹 Sử dụng cơ bản
```python
from nicecharts import fan_chart, line_chart, pie_chart

# Fan chart
fan_chart([30, 20, 50], labels=["A","B","C"], title="Fan Demo", outfile="fan.svg")

# Line chart
line_chart([1,2,3,4], [10,20,15,25], title="Line Demo", outfile="line.svg")

# Pie chart (full circle)
pie_chart([40,60], labels=["X","Y"], title="Pie Demo", outfile="pie.svg")
```

## 🔹 License
**MIT License**: Mọi người được phép sử dụng thư viện để học tập và cá nhân.

## 🔹 Liên hệ
GitHub: [https://github.com/username/nicecharts](https://github.com/username/nicecharts)
Email: [email của bạn]