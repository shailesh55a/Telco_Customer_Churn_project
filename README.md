# 📊 Telco Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to churn based on customer information. This project demonstrates an end-to-end machine learning workflow, including data preprocessing, exploratory data analysis, model training, evaluation, and deployment using Streamlit.

---

## 📌 Project Overview

Customer churn is a major challenge for telecom companies. This project uses machine learning algorithms to analyze customer data and predict the likelihood of churn. The trained model can help businesses identify at-risk customers and improve retention strategies.

---

## 🎯 Objectives

- Analyze customer churn patterns.
- Perform data cleaning and preprocessing.
- Train multiple Machine Learning models.
- Evaluate model performance.
- Deploy the best-performing model using Streamlit.

---

## 📂 Dataset

**Dataset Name:** WA_Fn-UseC_-Telco-Customer-Churn.csv

The dataset contains customer demographic information, account details, and service usage records.

**Target Variable:**
- `Churn`
  - Yes → Customer leaves the company
  - No → Customer stays with the company

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 📊 Project Workflow

1. Import Libraries
2. Load Dataset
3. Exploratory Data Analysis (EDA)
4. Data Cleaning
5. Feature Engineering
6. Data Visualization
7. Data Preprocessing
8. Train-Test Split
9. Model Training
10. Model Evaluation
11. Feature Importance
12. Save Best Model
13. Predict New Data
14. Deploy using Streamlit

---

## 🤖 Machine Learning Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

## 📈 Model Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- Feature Importance

---

## 🏆 Best Model

**Logistic Regression**

The Logistic Regression model achieved the best performance and was selected for deployment.

---

## 📊 Features Used

- Tenure
- Monthly Charges
- Total Charges
- Senior Citizen
- Partner
- Dependents
- Phone Service
- Paperless Billing

---

## 📁 Project Structure

```
Telco-Customer-Churn/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── customer_churn_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── customer_churn_prediction.ipynb
│
├── outputs/
│   ├── figures/
│   ├── predictions/
│   ├── feature_importance.csv
│   ├── model_comparison.csv
│   └── model_performance.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Telco-Customer-Churn.git
```

Move into the project directory:

```bash
cd Telco-Customer-Churn
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app/app.py
```

---

## 📷 Application

The Streamlit application allows users to:

- Enter customer information
- Predict customer churn
- View churn probability
- Display prediction results instantly

---

## 📌 Results

The trained model predicts whether a customer is likely to churn based on the selected customer features.

Example Output:

- Customer is likely to Stay ✅
- Customer is likely to Churn ⚠️
- Churn Probability

---

## 💡 Future Improvements

- Hyperparameter tuning
- Cross-validation
- XGBoost and LightGBM models
- Explainable AI using SHAP
- Cloud deployment
- Docker containerization

---

## 📚 Skills Demonstrated

- Data Analysis
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Model Evaluation
- Model Deployment
- Streamlit
- Python Programming
- Scikit-learn

---

## 👨‍💻 Author

**Shailesh Bahirat**

B.Sc. Artificial Intelligence & Machine Learning  
MIT Arts, Commerce & Science College, Alandi

LinkedIn: https://www.linkedin.com/in/your-linkedin


---

## ⭐ If you found this project helpful, please give it a star on GitHub!
