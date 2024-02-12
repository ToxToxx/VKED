from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest as ztest

sample = [32.8, 44.3, 29. , 23.5, 26.7, 39. , 36.2, 25.6, 37.9, 36.5, 43.8,
       59.7, 37.7, 38.4, 32.1, 28.2, 34.4, 22.1, 12.6, 26.9, 29.9, 55.5,
       34.1, 22.4, 25.4, 40. , 22.5, 38.8, 43.6, 34.4]
popmean = 37.
alternative= 'two-sided'

# a - выборка данных
# popmean - среднее, с которым хотим сравнить гипотезу
# alternative - вид альтернативной гипотезы

print(stats.ttest_1samp(sample, popmean, alternative = alternative))
#pvalue больше 5% - не можем отвергнуть гипотезу о том что  средние не равны
#для работы с некоторыми тестами нужна проверка на нормальность

#ПОСТРОЕНИЕ QQ ГРАФИКА
d = stats.lognorm(0.5, loc = 25, scale = 10)
sample_1 = d.rvs(size=300)#логнормальное

d = stats.norm(loc = 25, scale = 10)
sample_2 = d.rvs(size=300)#нормальное 

fig = plt.figure(figsize= (17,10))
ax1 = fig.add_subplot(221)
plt.hist(sample_1, bins = 20)
ax2 = fig.add_subplot(222) 
plt.hist(sample_2, bins = 20)
ax3 = fig.add_subplot(223)
stats.probplot(sample_1, dist = "norm", plot = plt)
ax3 = fig.add_subplot(224)
stats.probplot(sample_2, dist = "norm", plot = plt)
plt.show()