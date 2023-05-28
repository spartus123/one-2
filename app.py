from typing import List, Dict, Union
from flask import Flask, render_template, jsonify

app = Flask(__name__)





@app.route("/Apie mus")
def hello_world():
    return render_template('apie_mus.html')

@app.route("/Kontaktai")
def hello_world():
    return render_template('kontaktai.html')

@app.route("/Naujienos")
def hello_world():
    return render_template('naujienos.html')

@app.route("/Produktai")
def hello_world():
    return render_template('produktai.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
