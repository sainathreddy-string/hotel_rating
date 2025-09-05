import pickle
from flask import Flask, request, jsonify,app,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
#load the model
regmodel = pickle.load(open('stack.pkl', 'rb'))
sclmodel= pickle.load(open('scaler.pkl', 'rb'))



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["GET"])
def submit():
    data = {
        "score_cleanliness": request.args.get("score_cleanliness", type=float),
        "score_comfort": request.args.get("score_comfort", type=float),
        "score_facilities": request.args.get("score_facilities", type=float),
        "score_location": request.args.get("score_location", type=float),
        "score_staff": request.args.get("score_staff", type=float),
        "score_value_for_money": request.args.get("score_value_for_money", type=float),
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
