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



plt.figure(figsize=(8, 5))

sns.histplot(df["Age"], bins=20, kde=True)

plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()