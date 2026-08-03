import pandas as pd
from config import DATA_PATH

df = pd.read_csv(DATA_PATH)

print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("Columns")
print("=" * 50)
print(df.columns.tolist())

print("\n" + "=" * 50)
print("Data Types")
print("=" * 50)
print(df.dtypes)

print("\n" + "=" * 50)
print("Missing Values")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("Duplicate Rows")
print("=" * 50)
print(df.duplicated().sum())

print("\n" + "=" * 50)
print("Statistical Summary")
print("=" * 50)
print(df.describe())