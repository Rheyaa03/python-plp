import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")


print(df.head())


print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())


print("\nSummary statistics:\n", df.describe())


grouped = df.groupby('species').mean()
print("\nAverage values per species:\n", grouped)


print("\nObservation:")
print("- Iris-virginica tends to have longer petals and sepals.")


plt.figure(figsize=(8, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title('Sepal and Petal Length Trend')
plt.xlabel('Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='species', y='petal length (cm)', ci=None)
plt.title('Average Petal Length by Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.tight_layout()
plt.show()
