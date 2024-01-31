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

fig = plt.figure(figsize = (14,5))
ax1 = fig.add_subplot(221)
sns.kdeplot(df.Age.dropna())
ax2 = fig.add_subplot(222)
df['Age'].value_counts().sort_index().plot.line()
plt.show()

fig = plt.figure(figsize= (14,5))
sns.kdeplot(x = 'Age', y = 'Cholesterol', data = df, color = 'r', fill = False)
plt.show()

#гистограмма
fig = plt.figure(figsize= (14,5))
sns.histplot(df['Age'], kde= True)
plt.show()

#scatterplot
sns.jointplot(x = 'Age', y = 'Cholesterol', data = df, kind = 'hex', gridsize = 20)
plt.show()

plt.figure(figsize= (15,8))
sns.boxplot(y = 'Age', x = 'Cholesterol', 
            data = df[df.Age.isin(np.arange(20,40,1))], orient = 'h')
plt.show()

fig = plt.figure(figsize = (14,5))
sns.violinplot(y = 'MaxHR', x = 'Sex', hue = 'HeartDisease', split = True, data = df)
plt.show()

cols = ['Oldpeak', 'MaxHR', 'Cholesterol', 'RestingBP', 'Age']
sns_plot = sns.pairplot(df[cols])
plt.show()