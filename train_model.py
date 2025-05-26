import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from feature_extraction import extract_features

df = pd.read_csv('phishing_dataset.csv')

X = df['url'].apply(extract_features).tolist()
y = df['label']  # 1 = phishing, 0 = legit

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
joblib.dump(model, 'model.pkl')
