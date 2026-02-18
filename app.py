import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("churn_model.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Telecom Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

# User Inputs
tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=600.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# Simple encoding (adjust according to your training encoding)
contract_map = {"Month-to-month":0, "One year":1, "Two year":2}
internet_map = {"DSL":0, "Fiber optic":1, "No":2}
payment_map = {"Electronic check":0, "Mailed check":1, "Bank transfer":2, "Credit card":3}

features = np.array([[tenure,
                      monthly_charges,
                      total_charges,
                      contract_map[contract],
                      internet_map[internet_service],
                      payment_map[payment_method]]])

if st.button("Predict Churn"):
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"⚠ Customer is likely to churn (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer is likely to stay (Probability: {probability:.2f})")
