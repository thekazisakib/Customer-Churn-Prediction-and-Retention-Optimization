# Customer Churn Prediction and Retention Optimization: An End-to-End Machine Learning Solution

[Repository Link](https://github.com/thekazisakib/Customer-Churn-Prediction-and-Retention-Optimization)

## Overview

This project aims to predict customer churn and optimize retention strategies within the telecom industry. By building an end-to-end machine learning solution, the objective is to empower businesses with actionable insights, enabling proactive measures to retain customers and enhance revenue. This project showcases both data science skills and practical business impact, ideal for roles involving customer analytics, predictive modeling, and machine learning deployment.

## Project Objective

1. **Churn Prediction**: Accurately predict customers at risk of churning.
2. **Retention Strategy**: Provide insights to improve customer retention and reduce churn rates, increasing long-term revenue.

---

## Table of Contents

- [Data Description](#data-description)
- [Solution Approach](#solution-approach)
  - [Data Preprocessing](#data-preprocessing)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Feature Engineering](#feature-engineering)
  - [Model Selection & Training](#model-selection--training)
  - [Model Evaluation](#model-evaluation)
  - [Hyperparameter Tuning](#hyperparameter-tuning)
- [Business Impact](#business-impact)
- [Deployment](#deployment)
- [Future Scope](#future-scope)
- [Installation](#installation)
- [Conclusion](#conclusion)

---

## Data Description

The dataset used is the **Telecom Customer Churn Dataset** from Kaggle, containing **7,043 customer records** with **21 features**. Key features include:

- **Demographics** (e.g., gender, senior citizen status)
- **Account Details** (e.g., contract type, payment method)
- **Service Usage** (e.g., internet service type, monthly charges)
- **Target**: `Churn` (binary label: 1 if customer churned, 0 otherwise)

---

## Solution Approach

### 1. Data Preprocessing

- **Handling Missing Values:** Addressed any missing data to ensure model stability.
- **Encoding Categorical Features:** Applied encoding for categorical variables.
- **Scaling:** Standardized numerical features for optimal model performance.

### 2. Exploratory Data Analysis (EDA)

Conducted an EDA to discover data trends and correlations. Key insights included:

- Contract types and payment methods correlated significantly with churn rates.
- Monthly charges were higher for churned customers, indicating a potential pricing sensitivity.

### 3. Feature Engineering

New features were created to enhance model accuracy, such as:

- **Customer Tenure:** To gauge loyalty duration.
- **Engagement Scores:** Measures indicating the level of service usage.

### 4. Model Selection & Training

Several machine learning models were evaluated:

- **Logistic Regression**
- **Decision Trees**
- **Random Forests**
- **XGBoost**
- **KNeighborsClassifier**

**KNeighborsClassifier** provided the best balance of accuracy, precision, and recall.

### 5. Model Evaluation

Model performance was evaluated using:

- **Precision**: Ensures accurate churn predictions.
- **Recall**: Ensures all churn cases are detected.
- **ROC-AUC Score**: Measures the model’s predictive accuracy. KNeighborsClassifier achieved an **ROC-AUC of 0.96**.

### 6. Hyperparameter Tuning

Hyperparameters were optimized using **GridSearchCV**, resulting in a 2% improvement in accuracy.

---

## Business Impact

1. **Reduced Churn Rate:** Enables targeted retention efforts for high-risk customers.
2. **Revenue Optimization:** Retaining customers decreases acquisition costs and stabilizes revenue.
3. **Cost Efficiency:** Reduced churn minimizes marketing costs, as retaining customers is more cost-effective than acquiring new ones.

---

## Deployment

The solution is deployed using **Flask**. The web application provides:

- **Churn Prediction**: Accepts customer data inputs and outputs churn probability.
- **Retention Recommendations**: Offers actionable suggestions for customer retention.

---

## Future Scope

1. **Real-Time Data Integration:** To improve model prediction with current customer behavior.
2. **A/B Testing**: Evaluate retention strategies for continuous optimization.
3. **AutoML Integration**: Speed up model training and optimize accuracy.

---

## Installation

Clone the repository and install dependencies to run the project locally:

```bash
# Clone this repository
git clone https://github.com/thekazisakib/Customer-Churn-Prediction-and-Retention-Optimization

# Navigate to the project directory
cd Customer-Churn-Prediction-and-Retention-Optimization

# Install required packages
pip install -r requirements.txt

# Run the application
python app.py
```

---

## Repository Structure

```
├── config                # Configuration files
├── customer_churn        # Scripts for exception handling and utilities
├── notebook              # Notebooks for EDA and model training
├── Dockerfile            # Docker configuration for deployment
├── app.py                # Flask app for churn prediction
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── setup.py              # Project setup script
```

## Conclusion

This project demonstrates an end-to-end machine learning solution for predicting customer churn and optimizing retention strategies in the telecom sector. By leveraging data insights, this model helps businesses reduce churn, cut costs, and increase revenue, making it a valuable asset for customer-centric industries.
