# Telecom-Churn-Analysis-
📈 Telecom Customer Churn Analysis
This project is a simple, hands-on exploration of customer churn in a telecom dataset. The goal? To understand what makes customers leave and prepare the data for deeper analysis.

🔍 What does this script do?
Here's a quick rundown of what's happening:

Data Import: Loads the dataset from a .csv file containing customer info like monthly charges, tenure, and whether they’ve churned.

Data Cleaning:

The TotalCharges column had some blanks (empty strings) — these were replaced with zeros to avoid issues.

Converted TotalCharges from object to float so we can do proper numerical analysis later.

Missing Value Check: Checked how many missing values are present in each column using isnull().sum().

🎯 Why is this useful?
Before jumping into any fancy machine learning or visualizations, it's crucial to make sure your data is clean and ready to go. This script lays the foundation for churn prediction by handling common issues like incorrect data types and missing values.
