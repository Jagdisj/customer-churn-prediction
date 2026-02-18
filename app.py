import streamlit as st
import joblib
import pandas as pd

model = joblib.load("churn_model.pkl")

st.title("📊 Telecom Customer Churn Prediction")

tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 1000.0, 50.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 600.0)

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

if st.button("Predict"):

    input_df = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "Contract": [contract],
        "InternetService": [internet_service],
        "PaymentMethod": [payment_method]
    })

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]

    if prediction[0] == 1:
        st.error(f"⚠ Customer likely to churn (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer likely to stay (Probability: {probability:.2f})")

