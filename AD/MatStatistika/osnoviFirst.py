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

#Медиана - половина элементов меньше половина больше
median = np.median(gen_pop)
median_ln = np.median(gen_pop_ln)

fig = plt.figure(figsize=(15,7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha = 0.5)
line1 = plt.axvline(median, 
                    label = ('Медиана норм ' + str(round(median, 1))),
                    color = 'red',
                    linestyle = 'dashed',
                    linewidth = 3.5)
ax1.legend(handles = [line1], fontsize = 20)
plt.show()

fig = plt.figure(figsize=(15,7))
ax1 = plt.subplot(111)
plt.hist(gen_pop_ln, 50, alpha = 0.5)
line1 = plt.axvline(median_ln, 
                    label = ('Медиана логнорм ' + str(round(median, 1))),
                    color = 'red',
                    linestyle = 'dashed',
                    linewidth = 3.5)
ax1.legend(handles = [line1], fontsize = 20)
plt.show()

#Мода самое часто встречающееся значение во множестве наблюдений
dscr_lst = np.random.randint(0, 100, size = 1000)

fig = plt.figure(figsize= (15,7))
ax1 = plt.subplot(121)
plt.hist(dscr_lst, 100, alpha = 0.8)
plt.show()

mode = stats.mode(dscr_lst)
print("Мода: ", mode)

#Квантиль - значение, которое заданная случайная величина 
#не превышает с фиксированной вероятностью
#Если в процентах - перцентиль или процентиль

print('Np percentile: ', np.percentile(gen_pop, 75))
print('Scipy percentile: ', stats.scoreatpercentile(gen_pop, 75))

df_box_plot = pd.DataFrame()
df_box_plot['gen_pop'] = gen_pop
df_box_plot['gen_pop_ln'] = gen_pop_ln

fig = plt.figure(figsize = (15,7))
sns.boxplot(data = df_box_plot, orient = 'h')
plt.show()

#Среднее арифметическое
