import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, file) for file in
            os.listdir(images_path) if file.endswith(".jpg")]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    try:
        body = request.form['body']
        author = request.form['author']
        os.makedirs("tmp", exist_ok=True)
        r = requests.get(request.form['image_url'], stream=True)
        img = f"tmp/download-image-{random.randint(0, 10000000)}.jpg"
        if r.status_code == 200:
            with open(img, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
        else:
            return render_template('meme_form.html', error_message="Can't download image")
        path = meme.make_meme(img, body, author)
        os.remove(img)
        return render_template('meme.html', path=path)
    except Exception as ex:
        print(ex)
        return render_template('meme_form.html', error_message=str(ex))


if __name__ == "__main__":
    app.run()
