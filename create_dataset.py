import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of customers
n = 1500

# Customer IDs
customer_ids = [f"CUST_{i:04d}" for i in range(1, n + 1)]

# Customer information
age = np.random.randint(18, 65, n)

regions = np.random.choice(
    ["North", "South", "East", "West", "Central"],
    n
)

gender = np.random.choice(
    ["Male", "Female"],
    n
)

# Subscription information
plans = np.random.choice(
    ["Basic", "Standard", "Premium"],
    n,
    p=[0.35, 0.45, 0.20]
)

contract_types = np.random.choice(
    ["Monthly", "One Year", "Two Year"],
    n,
    p=[0.50, 0.30, 0.20]
)

payment_methods = np.random.choice(
    ["Credit Card", "Debit Card", "UPI", "Bank Transfer"],
    n
)

# Tenure in months
tenure = np.random.randint(1, 61, n)

# Monthly charges based on plan
monthly_charge = []

for plan in plans:
    if plan == "Basic":
        monthly_charge.append(np.random.uniform(20, 40))
    elif plan == "Standard":
        monthly_charge.append(np.random.uniform(40, 70))
    else:
        monthly_charge.append(np.random.uniform(70, 120))

monthly_charge = np.round(monthly_charge, 2)

# Number of customer support interactions
support_calls = np.random.poisson(2, n)

# Satisfaction score
satisfaction_score = np.clip(
    np.random.normal(7, 1.5, n),
    1,
    10
).round(1)

# Internet/service usage
usage_hours = np.random.randint(5, 101, n)

# Calculate estimated lifetime value
lifetime_value = np.round(
    monthly_charge * tenure,
    2
)

# Churn probability
churn_probability = (
    0.20
    + (contract_types == "Monthly") * 0.15
    + (plans == "Basic") * 0.08
    + (tenure < 12) * 0.12
    + (support_calls >= 4) * 0.10
    + (satisfaction_score < 6) * 0.15
)

# Random factor
random_factor = np.random.random(n)

# Churn
churn = np.where(
    random_factor < churn_probability,
    "Yes",
    "No"
)

# Churn reason
churn_reasons = []

for i in range(n):
    if churn[i] == "No":
        churn_reasons.append("Not Churned")
    else:
        reasons = [
            "High Price",
            "Poor Service",
            "Competitor Offer",
            "Lack of Features",
            "Customer Support"
        ]
        churn_reasons.append(
            np.random.choice(reasons)
        )

# Create DataFrame
df = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Age": age,
    "Gender": gender,
    "Region": regions,
    "Plan": plans,
    "Contract_Type": contract_types,
    "Payment_Method": payment_methods,
    "Tenure_Months": tenure,
    "Monthly_Charge": monthly_charge,
    "Support_Calls": support_calls,
    "Satisfaction_Score": satisfaction_score,
    "Usage_Hours": usage_hours,
    "Lifetime_Value": lifetime_value,
    "Churn": churn,
    "Churn_Reason": churn_reasons
})

# Save dataset
df.to_csv(
    "data/customer_churn_data.csv",
    index=False
)

print("Customer churn dataset created successfully!")
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nChurn Distribution:")
print(df["Churn"].value_counts())