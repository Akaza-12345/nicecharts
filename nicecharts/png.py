# 3. nicecharts/png.py
from PIL import Image
from io import BytesIO
import cairosvg

def svg_to_png(svg_text: str, outfile: str):
    """
    Convert SVG markup (string) to PNG file.
    Requires cairosvg: pip install cairosvg
    """
    png_bytes = cairosvg.svg2png(bytestring=svg_text.encode("utf-8"))
    with open(outfile, "wb") as f:
        f.write(png_bytes)