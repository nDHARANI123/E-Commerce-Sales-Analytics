import pandas as pd
import matplotlib.pyplot as plt

# Import final dataset
from data_preparation import merged_data

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 50)

# ============================
# Monthly Customer Acquisition
# ============================

monthly_customers = (
    merged_data
    .groupby("Month")["CustomerID"]
    .nunique()
    .reset_index()
)

print("\nMonthly Customer Acquisition")
print(monthly_customers)

# Correct month order
month_order = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

monthly_customers["Month"] = pd.Categorical(
    monthly_customers["Month"],
    categories=month_order,
    ordered=True
)

monthly_customers = monthly_customers.sort_values("Month")

# Plot
plt.figure(figsize=(10,5))
plt.plot(
    monthly_customers["Month"],
    monthly_customers["CustomerID"],
    marker="o"
)

plt.title("Monthly Customer Acquisition")
plt.xlabel("Month")
plt.ylabel("Unique Customers")
plt.grid(True)

plt.show()

# ==========================================
# Customer Retention Analysis
# ==========================================

print("\n" + "=" * 50)
print("CUSTOMER RETENTION ANALYSIS")
print("=" * 50)

customer_orders = (
    merged_data.groupby("CustomerID")["Transaction_ID"]
    .nunique()
    .reset_index()
)

customer_orders.rename(
    columns={"Transaction_ID": "Total_Orders"},
    inplace=True
)

customer_orders["Customer_Type"] = customer_orders["Total_Orders"].apply(
    lambda x: "Returning" if x > 1 else "New"
)

print(customer_orders.head())

print("\nCustomer Type Count")
print(customer_orders["Customer_Type"].value_counts())

# Plot
retention = customer_orders["Customer_Type"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    retention,
    labels=retention.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Retention Analysis")
plt.show()

# ==========================================
# Revenue Analysis
# ==========================================

print("\n" + "=" * 50)
print("REVENUE ANALYSIS")
print("=" * 50)

monthly_revenue = (
    merged_data.groupby("Month")["Invoice_Value"]
    .sum()
    .reset_index()
)

# Month order
month_order = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

monthly_revenue["Month"] = pd.Categorical(
    monthly_revenue["Month"],
    categories=month_order,
    ordered=True
)

monthly_revenue = monthly_revenue.sort_values("Month")

print(monthly_revenue)

# Plot
plt.figure(figsize=(10,5))
plt.bar(
    monthly_revenue["Month"],
    monthly_revenue["Invoice_Value"]
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(axis="y")

plt.show()

# ==========================================
# TOP 10 PRODUCT CATEGORIES BY REVENUE
# ==========================================

print("\n" + "=" * 50)
print("TOP 10 PRODUCT CATEGORIES")
print("=" * 50)

category_revenue = (
    merged_data.groupby("Product_Category")["Invoice_Value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

print(category_revenue)

# Plot
plt.figure(figsize=(10,6))
plt.bar(
    category_revenue["Product_Category"],
    category_revenue["Invoice_Value"]
)

plt.title("Top 10 Product Categories by Revenue")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(axis="y")

plt.show()