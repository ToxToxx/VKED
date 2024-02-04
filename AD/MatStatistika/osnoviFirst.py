import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd

np.random.seed(1234)

#ПРИМЕР ФОРМИРОВАНИЯ ГЕНЕРАЛЬНОЙ СОВОКУПНОСТИ НОРМ РАСПРЕДЕЛЕНИЯ

norm_rvl = stats.norm(loc = 15, scale = 10)
#scale - стандартное отклонение
#loc - среднее

#генерирует случайно значение из распределения norm_rvl
gen_pop = norm_rvl.rvs(size = 10000)

fig = plt.figure(figsize = (14,7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha = 0.5)
plt.show()

#ЛОГНОРМАЛЬНОЕ РАСПРЕДЕЛЕНИЕ

ln_distrib = stats.lognorm(0.5, loc = 25, scale = 10)
gen_pop_ln = ln_distrib.rvs(size = 10000)

fig = plt.figure(figsize = (14,7))
ax1 = plt.subplot(111)
plt.hist(gen_pop_ln, 50, alpha = 0.5)
plt.show()