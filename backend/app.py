from pyexpat import features

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

        # Extract features
        features = extract_features(url)
        # Generate dynamic reasons
        reasons = []

        if features["uses_https"] == 0:
            reasons.append("Website uses HTTP instead of HTTPS.")

        if features["has_at"] == 1:
            reasons.append("URL contains '@' symbol, commonly used in phishing URLs.")

        if features["suspicious_tld"] == 1:
            reasons.append("Website uses a suspicious top-level domain.")

        if features["keyword_flag"] == 1:
            reasons.append("URL contains phishing-related keywords.")

        if features["hyphen_in_host"] == 1:
            reasons.append("Domain contains hyphens which may indicate impersonation.")

        if features["numeric_domain"] == 1:
            reasons.append("Domain name contains numbers.")

        if features["length_url"] > 75:
            reasons.append("URL is unusually long.")

        if features["subdomain_depth"] >= 3:
            reasons.append("Website has multiple subdomains.")

        if features["digit_count"] > 6:
            reasons.append("URL contains many numeric characters.")

        if features["uppercase_count"] > 5:
            reasons.append("URL contains excessive uppercase letters.")

        if len(reasons) == 0:
            reasons.append("No suspicious URL characteristics detected.")
        df = pd.DataFrame([features])

        # Prediction
        prediction = model.predict(df)[0]

        # Prediction probabilities
        probabilities = model.predict_proba(df)[0]

        phishing_confidence = round(probabilities[1] * 100, 2)
        legitimate_confidence = round(probabilities[0] * 100, 2)

        if prediction == 1:
            confidence = phishing_confidence

            if confidence >= 90:
                risk_level = "HIGH"
            elif confidence >= 70:
                risk_level = "MEDIUM"
            else:
                risk_level = "LOW"

            prediction_text = "PHISHING"

        else:
            confidence = legitimate_confidence
            risk_level = "SAFE"
            prediction_text = "LEGITIMATE"

        return jsonify({
            "prediction": prediction_text,
            "confidence": confidence,
            "risk_level": risk_level,
            "phishing": int(prediction),
            "reasons": reasons
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
