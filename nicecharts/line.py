# 5. nicecharts/line.py
from .svg import SVG
from .png import svg_to_png

def line_chart(x, y, xlabel=None, ylabel=None, title=None,
               points=True, outfile="line.svg",
               width=600, height=400, color="black"):
    svg = SVG(width, height)

    margin = 50
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)

    def scale_x(v):
        return margin + (v - min_x) / (max_x - min_x) * (width - 2 * margin)

    def scale_y(v):
        return height - margin - (v - min_y) / (max_y - min_y) * (height - 2 * margin)

    svg.line(margin, margin, margin, height - margin, stroke="gray")
    svg.line(margin, height - margin, width - margin, height - margin, stroke="gray")

    if xlabel:
        svg.text(width // 2, height - 10, xlabel, size=14)
    if ylabel:
        svg.text(20, height // 2, ylabel, size=14)
    if title:
        svg.text(width // 2, 30, title, size=20)

    pts = [(scale_x(x[i]), scale_y(y[i])) for i in range(len(x))]

    for i in range(len(pts)-1):
        svg.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], stroke=color)

    if points:
        for px, py in pts:
            svg.circle(px, py, 4, fill=color, stroke=color)

    if outfile.lower().endswith(".png"):
        svg_to_png(svg.render(), outfile)
    else:
        svg.save(outfile)
