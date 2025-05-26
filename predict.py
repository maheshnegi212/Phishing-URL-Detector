import joblib
from feature_extraction import extract_features

model = joblib.load('model.pkl')

def predict_url(url):
    features = extract_features(url)
    prediction = model.predict([features])[0]
    return "Phishing" if prediction == 1 else "Legit"
