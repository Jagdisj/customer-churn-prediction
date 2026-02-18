## 📊 Customer Churn Prediction

Predicting customer churn is critical for telecom businesses to reduce revenue loss and improve customer retention strategies. This project builds and evaluates machine learning models to identify customers likely to leave the service.

## 🧠 Business Problem

Customer acquisition is significantly more expensive than customer retention. Telecom companies lose substantial revenue when customers discontinue their services (churn).
The objective of this project is to:
Predict whether a customer will churn
Identify key drivers influencing churn
Provide actionable insights to reduce churn rate
Support business teams with data-driven retention strategies

## 📂 Dataset Overview

Source: Telecom Customer Churn Dataset (Kaggle)
The dataset contains customer demographic details, account information, service usage patterns, and churn labels.

Key Features:
Customer demographics (gender, senior citizen, dependents)
Account details (tenure, contract type, payment method)
Service usage (internet service, streaming services, tech support)
Billing information (monthly charges, total charges)
Target variable: Churn (Yes/No)

## ⚙️ Tech Stack

Python
Pandas – Data manipulation
Scikit-learn – Model building and evaluation
Matplotlib – Data visualization

## 🔄 Project Workflow

Data Cleaning
Handled missing values
Converted categorical variables using encoding techniques
Standardized numerical features where required
Exploratory Data Analysis (EDA)
Churn distribution analysis
Feature correlation analysis
Tenure vs churn relationship
Contract type impact analysis
Feature Engineering
Encoding categorical variables
Scaling numerical variables
Feature selection based on importance
Model Development
Logistic Regression (baseline model)
Random Forest (ensemble model)
Model Evaluation
Accuracy
ROC-AUC
Confusion Matrix
Precision & Recall

## 📈 Model Performance Comparison

Model	Accuracy	ROC-AUC
Logistic Regression	82%	0.86
Random Forest	85%	0.89
Best Performing Model: Random Forest
The Random Forest model demonstrated superior predictive power and better class separation.

## 🔍 Key Business Insights

Customers with month-to-month contracts show significantly higher churn probability.
Short tenure customers are more likely to churn.
Higher churn observed among customers without tech support services.
Customers with higher monthly charges exhibit elevated churn risk.
Business Recommendation:
Offer long-term contract incentives.
Target new customers (tenure < 12 months) with engagement campaigns.
Bundle tech support services to improve retention.

## 📊 Evaluation Metrics Explained

Accuracy (85%): Overall correct predictions.
ROC-AUC (0.89): Strong ability to distinguish churn vs non-churn customers.
High ROC-AUC indicates strong ranking capability for risk scoring applications.

## 📊 Model Performance

### ROC Curve
<img width="678" height="520" alt="Screenshot 2026-02-17 111254" src="https://github.com/user-attachments/assets/63d3e916-9032-46c4-8b3f-a2c3399a309b" />


### Precision-Recall Curve
<img width="813" height="610" alt="Screenshot 2026-02-17 110959" src="https://github.com/user-attachments/assets/32c57c79-f912-453a-9c28-7a07ee820836" />



---

## 🔍 Feature Importance

<img width="986" height="661" alt="Screenshot 2026-02-17 111307" src="https://github.com/user-attachments/assets/8322be4e-8219-4464-9feb-b7408b92d79d" />


---

## 🧠 Model Explainability (SHAP)

### SHAP Summary Plot
<img width="681" height="348" alt="Screenshot 2026-02-17 111502" src="https://github.com/user-attachments/assets/34728ef2-d643-4090-9fd1-898a3825461c" />


### SHAP Force Plot (Single Customer)
<img width="597" height="302" alt="Screenshot 2026-02-17 111538" src="https://github.com/user-attachments/assets/e838214c-10c8-4b9b-aa33-e1b0b8aab546" />

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
git clone https://github.com/Jagdisj/customer-churn-prediction
cd customer-churn-prediction

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Notebook or Script
python churn_model.py


or open the Jupyter notebook:
jupyter notebook

## 📌 Future Improvements

Hyperparameter tuning (GridSearchCV)
Cross-validation for improved generalization
Model explainability using SHAP
Deployment using Flask / FastAPI
Real-time churn prediction API

## 📎 Conclusion

This project demonstrates an end-to-end machine learning pipeline for solving a real-world business problem. The model achieves strong predictive performance and provides actionable insights for reducing customer churn in telecom operations.

##   Telecom Customer Churn Prediction

🚀 **Live Demo:** https://customerchun.streamlit.app/

This is an end-to-end ML project deployed using Streamlit Cloud.

