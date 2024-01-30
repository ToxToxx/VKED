import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("E:/Programming/VKED/AD/SeabornAndPlotly/heart.csv")
df['Cholesterol'] = np.where(df['Cholesterol'] == 0, np.nan, df['Cholesterol'])
df['RestingBP'] = np.where(df['RestingBP'] == 0, np.nan, df['RestingBP'])
df['FastingBS'] = np.where(df['FastingBS'] == 0, np.nan, df['FastingBS'])

fig = plt.figure(figsize= (14, 5))
#pandas bar = seaborn countplot
sns.countplot(x = df['ChestPainType'])
plt.show()

fig = plt.figure(figuresize = (14,5))
ax1 = fig.add_subplot(221)
sns.kdeplot(df.Age.dropna())
ax2 = fig.add_subplot(222)
df['Age'].value_counts().sort_index().plot.line()
plt.show()