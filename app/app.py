from flask import Flask
from flask import Blueprint, request, render_template, jsonify

import sys, os
sys.path.insert(0,f'{os.getcwd()}/src')
import pipeline



app = Flask(__name__)



@app.route('/predict', methods=["POST", "GET"])
def predict():
    if not request.args:
        return {"status": "Failure", "message": "Nothing to predict"}
    text = request.args.get('tweet')
    prediction = pipeline.predict(text)
    abusive_scale = prediction["probability"][0]
    print (abusive_scale)
    is_abusive = 0
    if abusive_scale > 0.015:
        is_abusive = 1

    return {"status": "success", "is_abusive": str(is_abusive)}
    



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)