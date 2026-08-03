import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import DATA_PATH

# Load dataset
df = pd.read_csv(DATA_PATH)

# Set plot style
sns.set_style("whitegrid")

# Create figure
plt.figure(figsize=(6, 4))

# Plot Attrition counts
sns.countplot(data=df, x="Attrition")

# Add title
plt.title("Employee Attrition Distribution")

# Show plot
plt.show()

#======================================

plt.figure(figsize=(8, 5))

sns.histplot(df["Age"], bins=20, kde=True)

plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()

#--------------------------------------

plt.figure(figsize=(6,4))

sns.countplot(data=df, x="Gender")

plt.title("Gender Distribution")

plt.show()


#====================================

plt.figure(figsize=(7,4))
sns.countplot(data = df, x="Department")
plt.title("Department Distribution")
plt.xticks(rotation=20)
plt.show()


#+++++++++++++++++++++++++++++++

plt.figure(figsize=(12,5))

sns.countplot(data=df, x="JobRole")

plt.xticks(rotation=45)

plt.title("Job Role Distribution")

plt.show()



#+++++++++++++============

plt.figure(figsize=(8,5))

sns.histplot(df["MonthlyIncome"], bins=30, kde=True)

plt.title("Monthly Income Distribution")

plt.show()
