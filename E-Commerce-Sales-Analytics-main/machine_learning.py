import pandas as pd
from data_preparation import merged_data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 50)
print("MACHINE LEARNING")
print("=" * 50)

# Features
X = merged_data[[
    "Quantity",
    "Avg_Price",
    "Discount_pct",
    "GST",
    "Delivery_Charges"
]]

# Target
y = merged_data["Invoice_Value"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("\nR2 Score :", r2_score(y_test, y_pred))
print("RMSE :", mean_squared_error(y_test, y_pred) ** 0.5)

print("\nSample Predictions")
result = pd.DataFrame({
    "Actual": y_test.values[:10],
    "Predicted": y_pred[:10]
})

print(result)