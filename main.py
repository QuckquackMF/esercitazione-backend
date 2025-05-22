from flask import Flask, send_file, jsonify
from flask_cors import CORS # Import CORS
import json
import random

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

f = open('athletes.json') #Aprire il file json
data = json.load(f) #caricare l'oggetto dentro data
a = data['athletes'][random.randint(0, len(data['athletes']) - 1)] # Corrected random index
athletes_list = data['athletes']

@app.route("/")
def home():
    return "What is up"

@app.route("/all")
def athletes():
    return send_file("athletes.json")

@app.route("/random")
def random():
    return jsonify(a) # Use jsonify for JSON responses

@app.route("/cerca/<cognome>")
def cerca(cognome):
    found_athletes = [athlete for athlete in athletes_list if athlete['player_name'].lower() == cognome.lower()]
    if found_athletes:
        return jsonify(found_athletes)
    else:
        return jsonify({"message": f"Athlete with name '{cognome}' not found."})

if __name__ == "__main__":
    app.run(debug=True) # Enable debug mode for easier error tracking