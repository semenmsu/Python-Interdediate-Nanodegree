### Overview

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. It’s not that simple though! Your content team spent countless hours writing quotes in a variety of filetypes.

### How To Run

- python meme.py
- python meme.py --path image_path --body body --author author
- python app.py - to run flask app

### Structure

- MemeEngine - generate meme from image, body, author
- QuoteEngine - generate quotes base on file extensions
- meme.py - generate and save meme localy
- app.py - flask app for generating meme

### Dependencies

- python-docx
- Pillow
