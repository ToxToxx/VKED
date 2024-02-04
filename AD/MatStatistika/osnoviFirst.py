import matplotlib.pyplot as plt
import seaborn as sns
import scipy as stats
import numpy as np
import pandas as pd

np.random.seed(1234)

norm_rvl = stats.norm(loc = 15, scale = 10)
#scale - стандартное отклонение
#loc - среднее

#генерирует случайно значение из распределения norm_rvl
gen_pop = norm_rvl.rvs(size = 1000)

fig = plt.figure(figsize = (14,7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha = 0.5)
plt.show()