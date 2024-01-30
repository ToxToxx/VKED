import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E:/Programming/VKED/AD/PandasVisualization/heart.csv")
print(df.head(2))
print(df.info())
print(df.describe())

df['Cholesterol'] = np.where(df['Cholesterol'] == 0, np.nan, df['Cholesterol'])
df['RestingBP'] = np.where(df['RestingBP'] == 0, np.nan, df['RestingBP'])
df['FastingBS'] = np.where(df['FastingBS'] == 0, np.nan, df['FastingBS'])

fig = plt.figure(figsize = (14, 5))
df['ChestPainType'].value_counts().plot.bar()
plt.show()

fig = plt.figure(figsize= (14, 5))
df['ChestPainType'].value_counts().sort_index().plot.bar()
plt.show()

fig = plt.figure(figsize= (14, 5))
(df['ChestPainType'].value_counts() / len(df)).plot.bar()
plt.show()

print(df.groupby(['HeartDisease'])[['Age', 'Cholesterol']].mean())

df.groupby(['HeartDisease'])[['Age', 'Cholesterol']].mean().plot.bar(figsize = (14,5), stacked = False)
plt.show()

df.groupby(['HeartDisease'])[['Age', 'Cholesterol']].mean().plot.bar(figsize = (14,5), stacked = True)
plt.show()

df['Cholesterol_bin'] = df['Cholesterol'] // 10 * 10

fig = plt.figure(figsize= (14,5))
chart = df['Cholesterol_bin'].value_counts().sort_index().plot.line()
plt.show()