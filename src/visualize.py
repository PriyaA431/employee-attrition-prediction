import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import DATA_PATH

df = pd.read_csv(DATA_PATH)
sns.set_style("whitegrid")

def plot_attrition_distribution(df):
    # Create figure
    plt.figure(figsize=(6, 4))

    # Plot Attrition counts
    sns.countplot(data=df, x="Attrition")

    plt.title("Employee Attrition Distribution")
    plt.show()

#======================================
def plot_age_distribution(df):
    plt.figure(figsize=(8, 5))

    sns.histplot(df["Age"], bins=20, kde=True)

    plt.title("Age Distribution of Employees")
    plt.xlabel("Age")
    plt.ylabel("Number of Employees")

    plt.show()

#--------------------------------------
def plot_gender_distribution(df):
    plt.figure(figsize=(6,4))

    sns.countplot(data=df, x="Gender")

    plt.title("Gender Distribution")

    plt.show()


#====================================
def plot_department_distribution(df):
    plt.figure(figsize=(7,4))
    sns.countplot(data = df, x="Department")
    plt.title("Department Distribution")
    plt.xticks(rotation=20)
    plt.show()


#+++++++++++++++++++++++++++++++
def plot_job_role_distribution(df):
    plt.figure(figsize=(12,5))

    sns.countplot(data=df, x="JobRole")

    plt.xticks(rotation=45)

    plt.title("Job Role Distribution")

    plt.show()


#+++++++++++++============  
def plot_monthly_income_distribution(df):
    plt.figure(figsize=(8,5))

    sns.histplot(df["MonthlyIncome"], bins=30, kde=True)

    plt.title("Monthly Income Distribution")

    plt.savefig("reports/attrition_distribution.png")
    plt.show()

#=======================================
def plot_overtime_vs_attrition(df):
    plt.figure(figsize=(6,4))

    sns.countplot(
        data=df,
        x="OverTime",
        hue="Attrition"
    )

    plt.title("OverTime vs Attrition")
    plt.xlabel("OverTime")
    plt.ylabel("Employee Count")
    plt.show()

def plot_department_vs_attrition(df):
    plt.figure(figsize=(8,5))

    sns.countplot(
        data=df,
        x="Department",
        hue="Attrition"
    )
    plt.title("Department vs Attrition")
    plt.xticks(rotation=20)
    plt.show()

if __name__ == "__main__":
    # plot_attrition_distribution(df)
    # plot_age_distribution(df)
    # plot_gender_distribution(df)
    # plot_department_distribution(df)
    # plot_job_role_distribution(df)
    # plot_monthly_income_distribution(df)
    # plot_overtime_vs_attrition(df)
    plot_department_vs_attrition(df)


