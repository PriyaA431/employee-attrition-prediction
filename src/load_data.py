import pandas as pd
from config import DATA_PATH

df = pd.read_csv(DATA_PATH)

print("\n========== First 5 Rows ==========")
print(df.head())

print("\n========== Shape ==========")
print(df.shape)

print("\n========== Columns ==========")
print(df.columns)

print("\n========== Data Types ==========")
print(df.dtypes)
print(df.info())

print("\n========== Missing Values ==========")
print(df.isnull().sum())

print("\n========== Describe ==========")
print(df.describe())

print("\n========== Duplicate Rows ==========")
print(df.duplicated().sum())