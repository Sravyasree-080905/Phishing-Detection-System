from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from feature_extractor import extract_features

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load("phishing_model.pkl")

@app.route("/")
def home():
    return "Phishing Detection API is running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        features = extract_features(url)
        df = pd.DataFrame([features])

        prediction = model.predict(df)[0]

        # Probability of each class
        probabilities = model.predict_proba(df)[0]

        confidence = round(max(probabilities) * 100, 2)

        if confidence >= 90:
            risk_level = "HIGH"
        elif confidence >= 70:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        return jsonify({
            "prediction": "PHISHING" if prediction == 1 else "LEGITIMATE",
            "confidence": confidence,
            "risk_level": risk_level,
            "phishing": int(prediction)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
