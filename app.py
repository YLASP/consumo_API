from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api.api-ninjas.com/v1/motorcycles?make=kawasaki&model=ninja"
HEADERS = {"X-Api-Key": "==gquaHst56MQtBG0E"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/motorcycles")
def get_motorcycles():
    response = requests.get(API_URL, headers=HEADERS)
    if response.status_code == 200:
        motorcycles = response.json()
        filtered_motorcycles = [bike for bike in motorcycles if bike.get("displacement", 0) > 500]
        return jsonify(filtered_motorcycles)
    return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
