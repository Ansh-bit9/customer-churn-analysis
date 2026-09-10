import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 2. Clean TotalCharges so it can be used as a number
data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")

# 3. Remove duplicate rows
data = data.drop_duplicates()

# 4. Check the basic information
print("Total customers:", len(data))
print("Columns:", len(data.columns))

# 5. Calculate churn rate
churned_customers = data[data["Churn"] == "Yes"]
churn_rate = len(churned_customers) / len(data) * 100

print("Churned customers:", len(churned_customers))
print("Churn rate:", round(churn_rate, 2), "%")

# 6. Churn by contract
contract_churn = data.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nChurn rate by contract:")
print(contract_churn.round(2))

# 7. Churn by tenure group
data["TenureGroup"] = "25+ months"
data.loc[data["tenure"] <= 24, "TenureGroup"] = "13-24 months"
data.loc[data["tenure"] <= 12, "TenureGroup"] = "0-12 months"

tenure_churn = data.groupby("TenureGroup")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nChurn rate by tenure:")
print(tenure_churn.round(2))

# 8. Simple chart: churned vs retained
churn_count = data["Churn"].value_counts()

churn_count.plot(kind="bar", title="Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("churn_overview.png", dpi=150)
plt.close()
