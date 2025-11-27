# 2. nicecharts/svg.py
import math

class SVG:
    def __init__(self, width=600, height=400):
        self.width = width
        self.height = height
        self.elements = []

    def add(self, element: str):
        self.elements.append(element)

    def circle(self, cx, cy, r, fill="none", stroke="black", stroke_width=2):
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />')

    def line(self, x1, y1, x2, y2, stroke="black", stroke_width=2):
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}" />')

    def text(self, x, y, content, size=14, anchor="middle", color="black"):
        self.add(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}">{content}</text>')

    def polygon(self, points, fill="none", stroke="black", stroke_width=2):
        pts = " ".join([f"{x},{y}" for x, y in points])
        self.add(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />')

    def path(self, d, fill="none", stroke="black", stroke_width=2):
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />')

    def arc(self, cx, cy, r, start_angle, end_angle, stroke="black", stroke_width=2, fill="none"):
        x1 = cx + r * math.cos(math.radians(start_angle))
        y1 = cy + r * math.sin(math.radians(start_angle))
        x2 = cx + r * math.cos(math.radians(end_angle))
        y2 = cy + r * math.sin(math.radians(end_angle))
        large_arc = 1 if end_angle - start_angle > 180 else 0
        d = f"M {x1} {y1} A {r} {r} 0 {large_arc} 1 {x2} {y2}"
        self.path(d, stroke=stroke, stroke_width=stroke_width, fill=fill)

    def render(self):
        body = "\n".join(self.elements)
        return f"<svg width='{self.width}' height='{self.height}' xmlns='http://www.w3.org/2000/svg'>\n{body}\n</svg>"

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.render())