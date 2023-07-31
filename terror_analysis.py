import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = 'terrorism_dataset.csv'
terrorism_data = pd.read_csv(csv_file)

print(terrorism_data.head())

print(terrorism_data.describe())

print(terrorism_data.dtypes)

print(terrorism_data.isnull().sum())

plt.figure(figsize=(10, 6))
sns.countplot(x='Age', data=terrorism_data)
plt.xticks(rotation=90)
plt.title('Distribution of Age')  # Change the title accordingly
plt.show()
