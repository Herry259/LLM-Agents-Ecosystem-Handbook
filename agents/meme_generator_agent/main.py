"""
Meme Generator Agent
--------------------

This script creates a meme by overlaying a caption onto an image.  It
searches for a template image in the `templates` folder relative to the
script; if none is found it generates a blank white canvas.  The caption
is wrapped and drawn near the bottom of the image using Pillow.
"""

import argparse
import glob
import os
from typing import Optional

try:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore
except ImportError:
    Image = None  # type: ignore
    ImageDraw = None  # type: ignore
    ImageFont = None  # type: ignore


def load_template(directory: str = "templates") -> 'Image.Image':  # type: ignore
    """Load the first image in the templates directory or create a blank canvas."""
    if Image is None:
        raise RuntimeError(
            "Pillow is not installed. Please install it with `pip install pillow` to use this script."
        )
    for ext in ("*.png", "*.jpg", "*.jpeg"):
        files = glob.glob(os.path.join(directory, ext))
        if files:
            return Image.open(files[0]).convert("RGB")
    # Create a blank white image
    return Image.new("RGB", (600, 600), color=(255, 255, 255))


def wrap_text(text: str, draw: 'ImageDraw.Draw', font: 'ImageFont.FreeTypeFont', max_width: int) -> str:
    """Wrap text to fit within a given width on the image."""
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        width, _ = draw.textsize(test_line, font=font)
        if width <= max_width:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    lines.append(" ".join(current_line))
    return "\n".join(lines)


def generate_meme(caption: str, output_path: str = "generated_meme.png") -> None:
    if Image is None or ImageDraw is None or ImageFont is None:
        raise RuntimeError(
            "Pillow is not installed. Please install it with `pip install pillow` to use this script."
        )
    img = load_template()
    draw = ImageDraw.Draw(img)
    # Choose a default font.  If unavailable, Pillow will substitute a default.
    try:
        font = ImageFont.truetype("arial.ttf", size=32)
    except Exception:
        font = ImageFont.load_default()
    # Wrap caption
    max_width = img.width - 40
    wrapped = wrap_text(caption, draw, font, max_width)
    # Compute text height
    text_width, text_height = draw.multiline_textsize(wrapped, font=font)
    # Position text at bottom center
    x = (img.width - text_width) / 2
    y = img.height - text_height - 20
    # Draw outline for better readability
    outline_color = "black"
    for dx in [-2, -1, 0, 1, 2]:
        for dy in [-2, -1, 0, 1, 2]:
            draw.multiline_text((x + dx, y + dy), wrapped, font=font, fill=outline_color)
    # Draw the caption
    draw.multiline_text((x, y), wrapped, font=font, fill="white")
    img.save(output_path)
    print(f"Meme saved to {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Meme Generator Agent")
    parser.add_argument("--caption", type=str, required=True, help="Caption to overlay on the meme")
    parser.add_argument(
        "--output", type=str, default="generated_meme.png", help="Path to save the generated meme"
    )
    args = parser.parse_args()
    generate_meme(args.caption, args.output)


if __name__ == "__main__":
    main()