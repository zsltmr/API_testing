from flask import Flask, render_template
import requests
from datetime import datetime


app = Flask(__name__)


MY_LAT = 47.497913
MY_LONG = 19.040236


def iss_position():

    # get iss api json
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # get iss position
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    results = [iss_latitude, iss_longitude]
    return results


@app.route("/")
def home():
    coordinates = iss_position()
    return render_template("index.html", coordinates=coordinates)


if __name__ == '__main__':
    app.run(debug=True)