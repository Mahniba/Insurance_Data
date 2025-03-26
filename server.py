from flask import Flask, request, jsonify
from prediction_model import predict_price #import the function.

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    insurance_risk = float(data['insuranceRisk'])
    is_fleet = int(data['isFleet'])

    predicted_price = predict_price(insurance_risk, is_fleet) #use the function.

    return jsonify({'predictedPrice': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)