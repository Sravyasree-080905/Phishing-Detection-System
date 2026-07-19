import joblib

model = joblib.load("phishing_model.pkl")

print("Model Type:", type(model))

print("\nSupports predict_proba?:", hasattr(model, "predict_proba"))

print("\nAvailable Methods:")
print(dir(model))