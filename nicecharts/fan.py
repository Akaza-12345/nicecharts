from .svg import SVG
from .png import svg_to_png
import math

def fan_chart(values, labels=None, colors=None, title=None, outfile="fan.svg",
              width=600, height=400, full_circle=False):
    svg = SVG(width, height)
    cx, cy = width // 2, height // 2
    r = min(width, height) * 0.4

    if labels is None:
        labels = [f"S{i+1}" for i in range(len(values))]
    if colors is None:
        colors = ["#FF6666", "#66FF66", "#6666FF", "#FFCC66", "#66CCFF"] * 3

    total = sum(values)
    angle_start = 0 if full_circle else 180
    angle_range = 360 if full_circle else 180

    for i, v in enumerate(values):
        angle_end = angle_start + v / total * angle_range

        # Tính 4 điểm để tạo wedge
        x1 = cx + r * math.cos(math.radians(angle_start))
        y1 = cy + r * math.sin(math.radians(angle_start))
        x2 = cx + r * math.cos(math.radians(angle_end))
        y2 = cy + r * math.sin(math.radians(angle_end))

        # Path wedge
        large_arc = 1 if angle_end - angle_start > 180 else 0
        d = f"M {cx} {cy} L {x1} {y1} A {r} {r} 0 {large_arc} 1 {x2} {y2} Z"
        svg.path(d, fill=colors[i % len(colors)], stroke="white", stroke_width=2)

        # Label: góc giữa slice
        mid_angle = (angle_start + angle_end) / 2
        lx = cx + r * 0.6 * math.cos(math.radians(mid_angle))
        ly = cy + r * 0.6 * math.sin(math.radians(mid_angle))
        svg.text(lx, ly, labels[i], size=14, color="black")

        angle_start = angle_end

    if title:
        svg.text(cx, 30, title, size=22, color="black")

    if outfile.lower().endswith(".png"):
        svg_to_png(svg.render(), outfile)
    else:
        svg.save(outfile)

    return svg
