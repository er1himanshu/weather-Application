from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/weather_apps", methods=["POST", "GET"])
def get_data():
    if request.method == "POST":
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': request.form.get("city"),
            'appid': request.form.get("appid"),
            'units': request.form.get("units")
        }
        response = requests.get(url, params=params)
        data = response.json()
        return render_template("weather_result.html", data=data)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
