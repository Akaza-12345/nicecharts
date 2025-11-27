# 4. nicecharts/fan.py
from .svg import SVG
from .png import svg_to_png

def fan_chart(values, labels=None, colors=None, title=None, outfile="fan.svg",
              width=600, height=400, full_circle=False):
    svg = SVG(width, height)
    cx, cy = width // 2, height * 0.9
    max_r = min(width, height) * 0.4

    if labels is None:
        labels = [f"S{i+1}" for i in range(len(values))]
    if colors is None:
        colors = ["#FF6666", "#66FF66", "#6666FF", "#FFCC66", "#66CCFF"] * 3

    total = sum(values)
    angle_start = 0 if full_circle else 180
    angle_range = 360 if full_circle else 180

    for i, v in enumerate(values):
        portion = v / total
        angle_end = angle_start + portion * angle_range

        svg.arc(cx, cy, max_r, angle_start, angle_end, stroke="none", fill=colors[i])
        svg.arc(cx, cy, max_r, angle_start, angle_end, stroke="white", stroke_width=2)

        mid_angle = (angle_start + angle_end) / 2
        svg.text(cx, cy - max_r - 10, labels[i], size=14)

        angle_start = angle_end

    if title:
        svg.text(width // 2, 40, title, size=22)

    if outfile.lower().endswith(".png"):
        svg_to_png(svg.render(), outfile)
    else:
        svg.save(outfile)