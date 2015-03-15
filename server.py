from flask import Flask
import requests
from random import randint


GIPHY_CAT_URL = "http://api.giphy.com/v1/gifs/search?q=cute+cat&api_key=dc6zaTOxFJmzC&limit=100"


app = Flask(__name__)


@app.route("/cats/next")
def next_cat():
    response = requests.get(GIPHY_CAT_URL)
    json = response.json()
    num_responses = len(json['data'])  # get number of cats returned (for the off-chance it's less than the 100 cap)
    rand = randint(0, num_responses - 1)
    image_url = json['data'][rand]['images']['original']['mp4']
    return image_url


if __name__ == "__main__":
    app.run()
