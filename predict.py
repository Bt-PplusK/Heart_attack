import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model_C=0.001.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('heart_attack_risk')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    heart_attack_risk = y_pred >= 0.5

    result = {
        'heart_attack_risk_probability': float(y_pred),
        'heart_attack_risk': bool(heart_attack_risk)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
