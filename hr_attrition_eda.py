import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/hr_data.csv")

# Basic inspection
print(df.head())
print(df.info())
print(df.isnull().sum())

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Attrition distribution
sns.countplot(x="attrition", data=df)
plt.title("Employee Attrition Distribution")
plt.show()

# Attrition by department
sns.countplot(x="department", hue="attrition", data=df)
plt.xticks(rotation=45)
plt.title("Attrition by Department")
plt.show()

# Attrition vs Monthly Income
sns.boxplot(x="attrition", y="monthlyincome", data=df)
plt.title("Monthly Income vs Attrition")
plt.show()

# Key Insights:
# 1. Certain departments show higher attrition
# 2. Lower income employees tend to leave more
