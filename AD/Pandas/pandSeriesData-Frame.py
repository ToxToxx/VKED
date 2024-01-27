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
