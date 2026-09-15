# FUTURE_DS_02 – Customer Retention & Churn Analysis

## Future Interns – Data Science & Analytics Internship

### Task 2: Customer Retention & Churn Analysis

---

## 📌 Project Overview

This project analyzes customer data to identify churn patterns,
retention drivers, and customer lifetime trends.

The analysis focuses on understanding why customers leave a service,
which customer segments are at higher risk, and what actions can be
taken to improve customer retention.

---

## 🎯 Objectives

- Analyze customer churn patterns.
- Calculate churn and retention rates.
- Identify major churn reasons.
- Compare churn across contract types, plans, and regions.
- Analyze customer tenure and lifetime value.
- Compare satisfaction and support-call behavior.
- Segment customers according to churn risk.
- Provide business recommendations to reduce customer loss.

---

## 📊 Dataset

The project uses a simulated customer subscription dataset containing
1,500 customer records.

Important attributes include:

- Customer demographics
- Region
- Subscription plan
- Contract type
- Payment method
- Customer tenure
- Monthly charges
- Support calls
- Satisfaction score
- Usage hours
- Lifetime value
- Churn status
- Churn reason

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Excel

---

## 🔄 Analysis Process

The project follows these steps:

1. Load customer data
2. Inspect the dataset
3. Clean missing and duplicate records
4. Calculate customer retention KPIs
5. Analyze overall churn
6. Analyze churn by contract type
7. Analyze churn by subscription plan
8. Analyze churn by region
9. Analyze churn by customer tenure
10. Analyze churn reasons
11. Analyze customer lifetime value
12. Compare satisfaction and support calls
13. Perform customer risk segmentation
14. Generate business insights
15. Provide retention recommendations

---

## 📈 Key Analysis Areas

### Churn & Retention

The project calculates:

- Total customers
- Churned customers
- Retained customers
- Churn rate
- Retention rate

### Churn Drivers

Churn is analyzed based on:

- Contract type
- Subscription plan
- Region
- Tenure
- Churn reason
- Satisfaction
- Support calls

### Customer Lifetime Trends

Lifetime Value is analyzed across different customer tenure groups
and churn statuses.

### Risk Segmentation

Customers are categorized into:

- High Risk
- Medium Risk
- Low Risk

based on factors associated with customer churn.

---

## 📊 Visualizations

The project includes visualizations for:

- Overall churn distribution
- Churn by contract type
- Churn by plan
- Churn by region
- Churn by tenure
- Satisfaction vs churn
- Support calls vs churn
- Churn reasons
- Lifetime value vs churn
- Lifetime value by tenure
- Customer risk segmentation

---

## 💡 Business Recommendations

The analysis supports the following retention strategies:

- Focus retention campaigns on high-risk customers.
- Improve customer satisfaction and service quality.
- Monitor customers with frequent support calls.
- Address the major reasons responsible for churn.
- Provide targeted offers for customers using high-churn plans.
- Encourage longer-term contracts.
- Pay special attention to new customers with low tenure.
- Use customer risk segmentation for proactive retention campaigns.

---

## 📁 Project Structure

```text
FUTURE_DS_02/
│
├── data/
│   ├── customer_churn_data.csv
│   └── cleaned_customer_churn_data.csv
│
├── notebook/
│   └── customer_churn_analysis.ipynb
│
├── visualizations/
│   ├── churn_distribution.png
│   ├── churn_by_contract.png
│   ├── churn_by_plan.png
│   ├── churn_by_region.png
│   ├── churn_by_tenure.png
│   ├── satisfaction_vs_churn.png
│   ├── support_calls_vs_churn.png
│   ├── churn_reasons.png
│   ├── lifetime_value_vs_churn.png
│   ├── lifetime_value_by_tenure.png
│   └── customer_risk_segmentation.png
│
├── report/
│   ├── customer_churn_analysis.xlsx
│   └── churn_insights.txt
│
├── .gitignore
├── README.md
└── requirements.txt