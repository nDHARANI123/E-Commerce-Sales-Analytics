# E-Commerce Sales Analytics

E-Commerce Sales Analytics project using Python, Machine Learning and Power BI.

## Project Overview

This project analyzes e-commerce sales data to understand sales performance, customer behavior, revenue trends, customer retention and customer segments.

The project includes data preparation, exploratory data analysis, customer segmentation, machine learning and an interactive Power BI dashboard.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Machine Learning
- Power BI
- Excel
- CSV

## Project Workflow

1. Data Collection
2. Data Cleaning and Preparation
3. Data Merging
4. Exploratory Data Analysis
5. Customer Retention Analysis
6. Customer Segmentation
7. Machine Learning
8. Power BI Dashboard

## Key Analysis

### Customer Acquisition
Analyzed monthly customer acquisition to understand customer growth trends.

### Customer Retention
Customers were classified into New and Returning customers based on their number of orders.

### Revenue Analysis
Analyzed monthly revenue and identified top-performing product categories.

### Customer Segmentation
Customers were segmented into:
- Low Value
- Medium Value
- High Value

Segmentation was based on total customer revenue.

### Machine Learning
A Linear Regression model was implemented to predict Invoice Value using:
- Quantity
- Average Price
- Discount Percentage
- GST
- Delivery Charges

Model performance was evaluated using R² Score and RMSE.

## Power BI Dashboard

An interactive Power BI dashboard was created to visualize e-commerce sales performance and business insights.

## Project Files

- `data_preparation.py` - Data loading, cleaning, merging and invoice value calculation
- `eda.py` - Exploratory Data Analysis
- `customer_segmentation.py` - Customer segmentation
- `machine_learning.py` - Linear Regression model
- `main.py` - Main project execution file
- `final_dataset.csv` - Final processed dataset
- `customer_segmentation.csv` - Customer segmentation output
- `E-Commerce Sales Dashboard.pbix` - Power BI dashboard

## Conclusion

This project demonstrates an end-to-end e-commerce analytics workflow using Python, Machine Learning and Power BI to generate meaningful business insights from sales data.
