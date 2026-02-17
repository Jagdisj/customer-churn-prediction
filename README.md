# 🔥 Customer Churn Prediction using Machine Learning

An end-to-end machine learning project to predict customer churn and help businesses proactively reduce revenue loss.

This project focuses on maximizing churn detection using threshold tuning, AUC optimization, and SHAP-based explainability.

---

## 📌 Problem Statement

Customer churn is a high-risk business problem. Losing customers directly impacts recurring revenue.

The goal is to:
- Predict which customers are likely to churn
- Maximize recall for churn class
- Provide interpretable insights for business teams

---

## 🚀 Key Features

- Logistic Regression baseline model
- Random Forest & XGBoost comparison
- ROC-AUC based evaluation
- Threshold tuning (0.5 → 0.3)
- GridSearch hyperparameter optimization
- SHAP explainability (global + local)
- Business-driven model optimization

---

## 🛠 Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Matplotlib & Seaborn
- SHAP

---

## 📊 Model Performance

| Model | Accuracy | AUC |
|-------|----------|------|
| Logistic Regression | 0.79 | 0.83 |
| Random Forest | 0.79 | 0.82 |
| XGBoost | 0.79 | 0.82 |
| Tuned Logistic Regression | 0.78 | 0.84 |

---

## 🎯 Business Optimization

Since churn detection is a high-risk business problem, the probability threshold was tuned from **0.5 to 0.3**.

This improved churn recall from **52% to 91%**, significantly increasing churn capture rate.

Although accuracy decreased slightly, business impact improved by identifying more high-risk customers.

---

## 📈 ROC Curve Comparison

![ROC Curve](images/roc_curve.png)

---

## 📊 SHAP Feature Importance

![SHAP Summary](images/shap_summary.png)

Top churn drivers:
- Low tenure
- High monthly charges
- Fiber optic internet
- Short-term contracts

---

## 🧠 Model Explainability

SHAP was used to:
- Identify global feature importance
- Explain individual customer churn probability
- Provide interpretable business insights

---

## 📂 Project Workflow

1. Data Cleaning
2. Feature Encoding
3. Train-Test Split
4. Model Training
5. Hyperparameter Tuning
6. Threshold Optimization
7. Model Evaluation
8. SHAP Interpretation

---

## ⚙ Installation

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
