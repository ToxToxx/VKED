import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd

math_grades = [85, 90, 78, 92, 88, 85, 76, 98, 94, 87]

# Вычисление выборочного стандартного отклонения с помощью NumPy
std_deviation = np.std(math_grades, ddof=1)

# Вывод результата с округлением до трёх знаков после запятой
print(round(std_deviation, 3))

median = np.median(math_grades)
print(round(median, 1))
n = 5
sample = np.random.choice(math_grades, n, replace = False)

sample_mean = np.mean(sample)
print('Ср ариф выборки: ', sample_mean)