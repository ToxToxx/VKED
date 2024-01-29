import pandas as pd
import numpy as np

df = pd.read_csv("E:/Programming/VKED/AD/Pandas/orders.csv")

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.precision', 3)


print('Tail\n', df.tail())
print('Head\n', df.head())

print('Shape ', df.shape)
print('Columns', df.columns)
print('Describe\n', df.describe())
print('Describe object\n', df.describe(include=['object']))
print('City id count\n', df.city_id.value_counts(dropna = False)[:10])