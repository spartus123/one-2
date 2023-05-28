from typing import List, Dict, Union
from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUKTAI: List[Dict[str, Union[str, int]]] = [
    {
        'id': 1,
        'pavadinimas': "Logitech pele",
        'aprasymas': "bla bla",
        'kaina': 300,
    },
    {
        'id': 2,
        'pavadinimas': "Trust klaviatura",
        'aprasymas': "tuoj bus",
        'kaina': 400,
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', produktai=PRODUKTAI)

@app.route("/produktai")
def list_produktai():
    return jsonify(PRODUKTAI)

@app.route("/apie_mus")
def apie_mus():
    return render_template('apie_mus.html')

@app.route("/kontaktai")
def kontaktai():
    return render_template('kontaktai.html')

@app.route("/naujienos")
def naujienos():
    return render_template('naujienos.html')

@app.route("/produktai")
def produktai():
    return render_template('produktai.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
