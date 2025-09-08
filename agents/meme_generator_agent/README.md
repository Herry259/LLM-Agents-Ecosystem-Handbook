# Meme Generator Agent

This example is a playful **meme generator** that demonstrates how an agent can combine
images and text.  It asks the user for a short caption, then places the caption
on top of a chosen image.  The result is saved to disk so you can share it.

The agent uses the [Pillow](https://python-pillow.org) library for image
manipulation.  If Pillow is not installed or an image template is not found,
the script falls back to printing the meme as plain ASCII art.

## Setup

Install Pillow:

```bash
pip install pillow
```

Prepare a directory called `templates` inside this example’s folder and
place one or more `.jpg` or `.png` files that will serve as meme
backgrounds.  The script will pick the first image it finds.  If no
templates are present, a blank white image will be generated automatically.

## Usage

```bash
python main.py --caption "When the code finally works!"
```

The generated meme will be saved as `generated_meme.png` in the
current working directory.  You can open it using any image viewer.

## Extending the Agent

- Add more sophisticated text wrapping and font selection.
- Scrape trending meme templates from websites (subject to their terms of service).
- Integrate with a language model to suggest witty captions based on a theme.