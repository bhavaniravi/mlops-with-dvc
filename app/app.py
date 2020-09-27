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
    return {"status": "success", "is_abusive": str(prediction["infer"][0])}
    



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)