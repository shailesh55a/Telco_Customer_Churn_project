import joblib

model = joblib.load("../models/customer_churn_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

def predict(data):
    
    data = scaler.transform(data)
    
    predictions = model.predict(data)
    
    return predictions
