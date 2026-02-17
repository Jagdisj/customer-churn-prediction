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

## 📊 Model Performance

### ROC Curve
<img width="678" height="520" alt="Screenshot 2026-02-17 111254" src="https://github.com/user-attachments/assets/63d3e916-9032-46c4-8b3f-a2c3399a309b" />


### Precision-Recall Curve
****<img width="678" height="520" alt="Screenshot 2026-02-17 111254" src="https://github.com/user-attachments/assets/aed2a25b-98c1-4635-b00a-7c72ac6a8362" />


---

## 🔍 Feature Importance

<img width="986" height="661" alt="Screenshot 2026-02-17 111307" src="https://github.com/user-attachments/assets/8322be4e-8219-4464-9feb-b7408b92d79d" />


---

## 🧠 Model Explainability (SHAP)

### SHAP Summary Plot
<img width="681" height="348" alt="Screenshot 2026-02-17 111502" src="https://github.com/user-attachments/assets/34728ef2-d643-4090-9fd1-898a3825461c" />


### SHAP Force Plot (Single Customer)
<img width="681" height="348" alt="Screenshot 2026-02-17 111502" src="https://github.com/user-attachments/assets/9944217e-b5c8-4071-a173-0bbac745ad84" />



## ⚙ Installation

```bash
git clone https://github.com/jagdishj/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
