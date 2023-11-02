import pandas as pd

file_path="diabetes dataset/diabetes.csv"

df = pd.read_csv(file_path)

print(df.head())
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.isnull().sum())    
print(df['Outcome'].value_counts())
print(df.corr())

import seaborn as sns
import matplotlib.pyplot as plt

# Create a correlation matrix
correlation_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.show()


# Scatter plot of Glucose vs. Outcome
plt.figure(figsize=(8, 6))
plt.scatter(df['Glucose'], df['Outcome'], alpha=0.5, c='b')  # 'b' for blue
plt.title('Scatter Plot of Glucose vs. Outcome')
plt.xlabel('Glucose')
plt.ylabel('Outcome')
plt.grid(True)
plt.show()


import missingno as msno

msno.matrix(df) 