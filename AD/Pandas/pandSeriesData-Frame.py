import pandas as pd
import numpy as np


#Series - объект похожий на одномерный массив, отличается наличием ассоционированных меток, индексов вдоль каждого элемента
my_series = pd.Series([5,4,6,8,10,20])
print(my_series)
print(my_series.index)
print(my_series.values)

my_series2 = pd.Series([1, 2, 3, 4, 5,],
                       index = ["a", "b", "c", "d", "f"])

print("второй массив\n", my_series2)
print(my_series[2])
print(my_series2["d"])

mask = my_series > 6
print("Маска \n", mask)
print(my_series[mask])

my_series2[ ["a", "b", "c"] ] = 5
print("измененный\n", my_series2)
print(my_series[my_series < 8])

my_series3 = pd.Series({ "a" : 1, "b" : 2, "c" : 3, "d" : 4, "g" : 5})
print("Третий\n", my_series3)
my_series3.name = "bukvi"
my_series3.index.name = "privet"
print("Изменение\n", my_series3)

#pandas DataFrame = таблица
print("             DATAFRAME           ")
df = pd.DataFrame({
    'name': ['Alexey', 'Maxim', 'Sergey'],
    'height': [188, 170, 177],
    'weight': [85, 68, 77]
})
print(df)
print(df["height"])
print(df[['name']])
print(df.weight)
df.index = ["Lexa", "Max", "Serg"]
print(df)

#loc и iloc
print(df.loc["Max"])
print(df.iloc[2])
print(df.loc[["Max", "Lexa"],"name"])
print(df.iloc[[0,1], 2])
