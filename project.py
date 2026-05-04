import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv(r"C:\Users\mdkas\OneDrive\Desktop\numpy\NUMPY ARRAY PROPERTIES\Employee Dataset\Employee.csv")
#checking top part of dataset
print(df.head())

#checking the missing values
print("missing values in each column")
print(df.isnull().sum())

#checking duplicate values
print("duplicate values")
print(df.duplicated().sum())

#cleaning duplicate values
df.drop_duplicates(inplace=True)
#after deleting duplicates
print("duplicates deleted")
print(df.duplicated().sum())
#checking data types
print(df.info())
#checking outliers
print(df.describe())
#saving the data
df.to_csv('cleaned_Employee_Data.csv', index=False)
print('data cleaning completed! save as "cleaned_Employee_Data.csv"')