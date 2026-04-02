import numpy as np
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class AnomalyDetector:

    # 🔹 Load pretrained model
    def load_model(self):
        self.model = joblib.load("anomaly_model.pkl")
        self.scaler = joblib.load("scaler.pkl")

    # 🔹 Dynamic model
    def train_model(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.scaler = StandardScaler()

    # 🔹 Predict using pretrained model
    def predict_pretrained(self, data):
        X_scaled = self.scaler.transform(data)
        preds = self.model.predict(X_scaled)
        return np.where(preds == -1, 1, 0)

    # 🔹 Predict using dynamic model
    def predict_dynamic(self, data):
        X_scaled = self.scaler.fit_transform(data)
        self.model.fit(X_scaled)
        preds = self.model.predict(X_scaled)
        return np.where(preds == -1, 1, 0)