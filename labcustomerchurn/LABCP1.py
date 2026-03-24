'''
LAB CP1  — Profile the Customer Dataset
Goal: Understand structure and quality before any transformation
Prereq: customer_churn.csv available

'''
import pandas as pd

df = pd.read_csv("D:\\prodapt2026MarApril\\datasetforlabs\\customer_churn.csv")
#print(df.head())
print(df.shape)   # expect (7043, 21)
print(df.dtypes)
print(df.isnull().sum())
print(df["Churn"].value_counts(normalize=True).round(3) * 100)
print(pd.to_numeric(df["TotalCharges"], errors="coerce").isna().sum())  # ~11 blanks