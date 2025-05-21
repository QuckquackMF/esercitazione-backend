from flask import Flask, send_file
import json
import random

app = Flask(__name__)

f = open('athletes.json') #Aprire il file json
data = json.load(f) #caricare l'oggetto dentro data
a = data['athletes'][random.randint(1,10)]

@app.route("/")
def home():
    return "What is up"

@app.route("/all")
def athletes():
    return send_file("athletes.json")

@app.route("/random")
def random():
    return a

@app.route("/cerca")
def cerca():
    return "Ciao"



if __name__ == "__main__":
    app.run()