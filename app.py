from flask import Flask, request, jsonify
from classifier import get_prediction


app=Flask(__name__)
@app.route("/predict-digit",methods=["POST"])

def predict_data():
    image=request.files.get("digit")
    predict=get_prediction(image)
    return jsonify({
        "prediction":predict
    }),200

if __name__ == "__main__":
    app.run(debug=True)