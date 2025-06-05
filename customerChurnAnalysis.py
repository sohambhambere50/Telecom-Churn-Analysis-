import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Administrator\Desktop\Churn Analysis\Customer Churn.csv")
# print(df.head())
# print(df.info())
df['TotalCharges'] = df['TotalCharges'].replace(" ","0")
df['TotalCharges'] = df['TotalCharges'].astype("float")
# print(df.info())
print(df.isnull().sum())