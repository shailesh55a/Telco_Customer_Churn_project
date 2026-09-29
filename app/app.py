import streamlit as st
import pandas as pd
import joblib
import os


# Get project root directory

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model & Scaler Paths

MODEL_PATH = os.path.join(BASE_DIR, "models", "customer_churn_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")


# Check files exist

if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found:\n{MODEL_PATH}")
    st.stop()

if not os.path.exists(SCALER_PATH):
    st.error(f"Scaler file not found:\n{SCALER_PATH}")
    st.stop()


# Load model & scaler

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# Streamlit Page

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

st.subheader("Enter Customer Details")


# User Inputs

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=72,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0
)

senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
phone = st.selectbox("Phone Service", ["No", "Yes"])
paperless = st.selectbox("Paperless Billing", ["No", "Yes"])


# Prediction

if st.button("Predict Churn"):

    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "SeniorCitizen": [1 if senior == "Yes" else 0],
        "Partner": [1 if partner == "Yes" else 0],
        "Dependents": [1 if dependents == "Yes" else 0],
        "PhoneService": [1 if phone == "Yes" else 0],
        "PaperlessBilling": [1 if paperless == "Yes" else 0]
    })

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

    st.metric("Churn Probability", f"{probability:.2%}")
