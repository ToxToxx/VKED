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