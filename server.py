from flask import Flask
import requests
from random import randint


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/cats/next")
def next_cat():
    giphy_cat_url = "http://api.giphy.com/v1/gifs/search?q=cute+cat&api_key=dc6zaTOxFJmzC&limit=100"
    response = requests.get(giphy_cat_url)
    json = response.json()
    rand = randint(0, 99)
    image_url = json['data'][rand]['images']['original']['mp4']
    return image_url


if __name__ == "__main__":
    app.run()
