import pandas as pd

from data_preparation import merged_data

print("=" * 50)
print("CUSTOMER SEGMENTATION")
print("=" * 50)

customer_summary = (
    merged_data.groupby("CustomerID")
    .agg(
        Total_Revenue=("Invoice_Value", "sum"),
        Total_Orders=("Transaction_ID", "nunique"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
)

customer_summary["Segment"] = pd.qcut(
    customer_summary["Total_Revenue"],
    q=3,
    labels=["Low Value", "Medium Value", "High Value"]
)

print(customer_summary.head())

print("\nCustomer Segment Count")
print(customer_summary["Segment"].value_counts())

# Save customer segmentation result
customer_summary.to_csv("customer_segmentation.csv", index=False)

print("\nCustomer segmentation file created successfully!")