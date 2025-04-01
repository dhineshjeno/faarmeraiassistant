import os
import requests
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load the API key from the .env file
API_KEY = os.getenv("WEATHER_API_KEY")  # Make sure your .env file has this key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather/<city>')
def weather(city):
    url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to get weather data"}), 400

if __name__ == "__main__":
    app.run(debug=True)
