
from flask import Flask, render_template
import requests

QUOTES_URL = 'https://api.quotable.io/random'

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    quote = "Light tomorrow with today!"
    author = "Elizabeth Browning"
    response = requests.get(QUOTES_URL)
    if response.status_code == requests.codes.ok:
        data = response.json()
        quote = data.get("content")
        author = data.get("author")
    return render_template('index.html', quote=quote, author=author)


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
