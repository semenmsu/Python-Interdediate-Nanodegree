import os
from PIL import Image, ImageFont, ImageDraw
import random
from random import randint
import pathlib

def break_fix(text, width, font, draw):
    if not text:
        return
    lo = 0
    hi = len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        t = text[:mid]
        w, h = draw.textsize(t, font=font)
        if w <= width:
            lo = mid
        else:
            hi = mid - 1
    t = text[:lo]
    w, h = draw.textsize(t, font=font)
    yield t, w, h
    yield from break_fix(text[lo:], width, font, draw)

def fit_text(img, text, color, font):
    width = img.size[0] - 2
    draw = ImageDraw.Draw(img)
    pieces = list(break_fix(text, width, font, draw))
    height = sum(p[2] for p in pieces)
    if height > img.size[1]:
        raise ValueError("text doesn't fit")
    y = (img.size[1] - height) // 2
    for t, w, h in pieces:
        x = (img.size[0] - w) // 2
        draw.text((x, y), t, font=font, fill=color)
        y += h

class MemeEngine:
    def __init__(self, tempdir):
        self.tempdir = tempdir
        os.makedirs(tempdir, exist_ok=True)

    def make_meme(self, img_path, body, author, width=500):
        img = Image.open(img_path)
        w, h = img.size
        ratio = width/float(w)
        height = int(ratio*float(h))
        img = img.resize((width, height), Image.NEAREST)
        font_path = pathlib.Path(__file__).parent.parent.resolve() / "media/timesnewarial.ttf"
        font = ImageFont.truetype(str(font_path), 40)
        font2 = ImageFont.truetype(str(font_path), 20)
        x, y = random.randint(0, int(width/4)), \
            random.randint(0, int(height/1.4))
        x2, y2 = x, y + 45
        #draw = ImageDraw.Draw(img)
        #draw.text((x, y), body, (255, 255, 255), font=font)
        #draw.text((x2, y2), f"  -{author}", (255, 255, 255), font=font2)
        fit_text(img, f"{body} \n -{author}", (255,255,255), font)
        #fit_text(img, f"  -{author}", (255,255,255), font2)
        new_meme_path = os.path.join(self.tempdir,
                                     "img-"+str(randint(0, 1e10))+".jpg")
        img.save(new_meme_path)
        return new_meme_path
