import pandas as pd

# ============================
# Load Datasets
# ============================

online_sales = pd.read_csv("data/Online_Sales.csv")
customers = pd.read_excel("data/CustomersData.xlsx")
discount = pd.read_csv("data/Discount_Coupon.csv")
marketing = pd.read_csv("data/Marketing_Spend.csv")
tax = pd.read_excel("data/Tax_amount.xlsx")

print("All datasets loaded successfully!")

# ============================
# Display First 5 Records
# ============================

print("\n========== ONLINE SALES ==========")
print(online_sales.head())

print("\n========== CUSTOMERS ==========")
print(customers.head())

print("\n========== DISCOUNT ==========")
print(discount.head())

print("\n========== MARKETING ==========")
print(marketing.head())

print("\n========== TAX ==========")
print(tax.head())

# ============================
# Shape
# ============================

print("\n========== SHAPE ==========")

print("Online Sales :", online_sales.shape)
print("Customers :", customers.shape)
print("Discount :", discount.shape)
print("Marketing :", marketing.shape)
print("Tax :", tax.shape)

# ============================
# Dataset Information
# ============================

print("\n========== ONLINE SALES INFO ==========")
online_sales.info()

print("\n========== CUSTOMERS INFO ==========")
customers.info()

print("\n========== DISCOUNT INFO ==========")
discount.info()

print("\n========== MARKETING INFO ==========")
marketing.info()

print("\n========== TAX INFO ==========")
tax.info()

# ============================
# Missing Values
# ============================

print("\n========== MISSING VALUES ==========")

print("\nOnline Sales")
print(online_sales.isnull().sum())

print("\nCustomers")
print(customers.isnull().sum())

print("\nDiscount")
print(discount.isnull().sum())

print("\nMarketing")
print(marketing.isnull().sum())

print("\nTax")
print(tax.isnull().sum())

# ============================
# Duplicate Values
# ============================

print("\n========== DUPLICATE VALUES ==========")

print("Online Sales :", online_sales.duplicated().sum())
print("Customers :", customers.duplicated().sum())
print("Discount :", discount.duplicated().sum())
print("Marketing :", marketing.duplicated().sum())
print("Tax :", tax.duplicated().sum())

# ============================
# DATA CLEANING
# ============================

print("\n========== DATA CLEANING ==========")

# Remove extra spaces from column names
online_sales.columns = online_sales.columns.str.strip()
customers.columns = customers.columns.str.strip()
discount.columns = discount.columns.str.strip()
marketing.columns = marketing.columns.str.strip()
tax.columns = tax.columns.str.strip()

# Convert dates
online_sales["Transaction_Date"] = pd.to_datetime(
    online_sales["Transaction_Date"],
    format="%Y%m%d"
)

marketing["Date"] = pd.to_datetime(marketing["Date"])

# Create Month column
online_sales["Month"] = online_sales["Transaction_Date"].dt.strftime("%b")

print("\n========== DATA TYPES AFTER CONVERSION ==========")

print("\nOnline Sales:")
print(online_sales.dtypes)

print("\nMarketing:")
print(marketing.dtypes)

print("\n========== CLEANED ONLINE SALES ==========")
print(online_sales.head())

print("\n========== CLEANED MARKETING ==========")
print(marketing.head())

# ============================
# DATA MERGING
# ============================

print("\n========== DATA MERGING ==========")

# Merge Customers
merged_data = pd.merge(
    online_sales,
    customers,
    on="CustomerID",
    how="left"
)

print("\nAfter Merging Customers:")
print(merged_data.head())

print("\nShape :", merged_data.shape)

print("\nMissing Values:")
print(merged_data.isnull().sum())

# ============================
# MERGE TAX
# ============================

merged_data = pd.merge(
    merged_data,
    tax,
    on="Product_Category",
    how="left"
)

print("\n========== AFTER MERGING TAX ==========")
print(merged_data.head())

print("\nShape :", merged_data.shape)

print("\nMissing Values:")
print(merged_data.isnull().sum())

# ============================
# CHECK DISCOUNT COLUMNS
# ============================

print("\nDiscount Columns:")
print(discount.columns)

# ============================
# MERGE DISCOUNT
# ============================

merged_data = pd.merge(
    merged_data,
    discount,
    on=["Month", "Product_Category"],
    how="left"
)

print("\n========== AFTER MERGING DISCOUNT ==========")
print(merged_data.head())

print("\nShape :", merged_data.shape)

print("\nMissing Values:")
print(merged_data.isnull().sum())

# ============================
# FILL MISSING DISCOUNT VALUES
# ============================

merged_data["Discount_pct"] = merged_data["Discount_pct"].fillna(0)
merged_data["Coupon_Code"] = merged_data["Coupon_Code"].fillna("No Coupon")

# ============================
# MERGE MARKETING DATA
# ============================

merged_data = pd.merge(
    merged_data,
    marketing,
    left_on="Transaction_Date",
    right_on="Date",
    how="left"
)

print("\n========== AFTER MERGING MARKETING ==========")
print(merged_data.head())

print("\nShape :", merged_data.shape)

# ============================
# INVOICE VALUE CALCULATION
# ============================

merged_data["Invoice_Value"] = (
    (merged_data["Quantity"] * merged_data["Avg_Price"])
    * (1 - (merged_data["Discount_pct"] / 100))
    * (1 + merged_data["GST"])
) + merged_data["Delivery_Charges"]

print("\n========== INVOICE VALUE ==========")
print(
    merged_data[
        [
            "Quantity",
            "Avg_Price",
            "Discount_pct",
            "GST",
            "Delivery_Charges",
            "Invoice_Value",
        ]
    ].head()
)

# Final merged dataset
merged_data = merged_data

merged_data.to_csv("final_dataset.csv", index=False)

print("Final dataset exported successfully!")