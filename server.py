from flask import Flask
import requests


GIPHY_CAT_URL = "http://api.giphy.com/v1/gifs/random?tag=cute+cat&api_key=dc6zaTOxFJmzC"


app = Flask(__name__)


@app.route("/cats/random")
def next_cat():
    response = requests.get(GIPHY_CAT_URL)
    json = response.json()
    image_url = json['data']['image_mp4_url']
    return image_url


if __name__ == "__main__":
    app.run()
