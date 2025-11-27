# 🎨 nicecharts

**nicecharts** is a lightweight, zero-matplotlib Python charting library that can generate  
**SVG** and **PNG** images directly — perfect for embedding into reports, dashboards, and automation tools.

It currently includes:
- **Fan charts** (curved arcs, colored sections, labels)
- **Line charts** (with grid, axis labels, points, titles)

---

## ✨ Features

- ✔️ No matplotlib required  
- ✔️ Pure Python rendering  
- ✔️ SVG output (resolution-independent)  
- ✔️ PNG output (via Pillow)  
- ✔️ Easy, intuitive API like:

```python
import nicecharts.fan as fan

fan.fan_chart(
    values=[30, 20, 50],
    labels=["A", "B", "C"],
    colors=["#ff9999", "#99ff99", "#9999ff"],
    title="Fan Example",
    outfile="fan.svg"
)
