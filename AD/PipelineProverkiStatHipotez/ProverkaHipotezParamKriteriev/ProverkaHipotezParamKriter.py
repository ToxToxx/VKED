from scipy import stats
from sklearn import datasets
from statsmodels.stats.weightstats import ztest as ztest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



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

fig = plt.figure(figsize= (14,8))
ax1 = fig.add_subplot(221)
plt.hist(sample_1, bins = 20)
ax2 = fig.add_subplot(222) 
plt.hist(sample_2, bins = 20)
ax3 = fig.add_subplot(223)
stats.probplot(sample_1, dist = "norm", plot = plt)
ax3 = fig.add_subplot(224)
stats.probplot(sample_2, dist = "norm", plot = plt)
plt.show()

#КРИТЕРИЙ ШАПИРО УИЛКО применяется до 50 наблюдений
d = stats.lognorm(0.5, loc = 25, scale = 10)
sample_1 = d.rvs(size=35)

d = stats.norm(loc = 25, scale = 10)
sample_2 = d.rvs(size=30)

print(stats.shapiro(sample_1))#отвергается
print(stats.shapiro(sample_2))#принимается гипотеза ибо при заданном значении p > 0.05


#РЕШЕНИЕ ЗАДАЧИ ПРО КОМПЬЮТЕРЫ. ИСПОЛЬЗУЕТСЯ КРИТЕРИЙ СТЬЮДЕНТА
sample_mean = 102
mu = 90
n = 20
sample_std = 15

t = (sample_mean - mu) / (sample_std/np.sqrt(n))
print('t ', t)

t_crit = stats.t.ppf(1-0.05, n)
print('t критическое ', t_crit)

fig = plt.figure(figsize= (10,4))
xs = np.linspace(-5,5,1000)
plt.plot(xs, stats.t.pdf(xs, n - 1))
plt.axvline(t_crit, color='red', linestyle='dashed', linewidth=3, label = 't-крит')
plt.axvline(t, color='blue', linestyle='dashed', linewidth=1,label = 't-наблюдаемое')
plt.legend()
plt.show()
#Вывод - новые компьютеры влияют на время сессии t наблюдаемое намного выше t критического

#ДВУВЫБОРОЧНЫЙ КРИТЕРИЙ С БОЛЬШИМ ЧИСЛОМ НАБЛЮДЕНИЙ
sample_1 = [32.8, 44.3, 29. , 23.5, 26.7, 39. , 36.2, 25.6, 37.9, 36.5, 43.8,
       59.7, 37.7, 38.4, 32.1, 28.2, 34.4, 22.1, 12.6, 26.9, 29.9, 55.5,
       34.1, 22.4, 25.4, 40. , 22.5, 38.8, 43.6, 34.4]
sample_2 = [34.2, 35.4, 53.2, 37.8, 34.6, 31.4, 35.8, 40.4, 32.4, 29.8, 30.9,
       52.5, 44. , 32.3, 39.3, 31.7, 48.3, 34.7, 41.1, 52.3, 38.8, 55.8,
       35.4, 32.3, 31.4, 37.6, 33.3, 42.9, 48.9, 39.2]
alternative= 'two-sided'

#Z - test
print('Z test', ztest(sample_1, sample_2,alternative = alternative)) 

# t-test
print('t test', stats.ttest_ind(sample_1, sample_2, alternative = alternative))

# W-test
print('W test', stats.ttest_ind(sample_1, sample_2, alternative = alternative, equal_var = False))

#отвергаем 0 гипотезу все 3 статистики об этом говорят

#РЕШЕНИЕ ЗАДАЧИ О ФИЛЬМАХ
ratings_1 = [
       4.3, 5.8, 5.7, 5.4, 5.1, 5.7, 5.1, 5.4, 5.1, 4.6, 5.1, 4.8, 5. ,
       5. , 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5. , 5.5, 4.9, 4.4,
       5.1, 5. , 4.5, 4.4, 5. , 5.1, 4.8, 5.1, 4.6, 5.3, 5. , 7. , 6.4,
             3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3. ,
       3. , 4. , 4.4, 3.9, 3.5, 3.8, 3.8, 3.4, 3.7, 3.6,
       6.8, 6.7, 6.7, 6.3, 6.5, 6.2, 5.9]

ratings_2 = [3.5, 3. , 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3. ,
       3. , 4. , 4.4, 3.9, 3.5, 3.8, 3.8, 3.4, 3.7, 3.6, 3.3, 3.4, 3. ,
       3.4, 3.5, 3.4, 3.2, 3.1, 3.4, 4.1, 4.2, 3.1, 3.2, 3.5, 3.6, 3. ,
       3.4, 3.5, 2.3, 3.2, 3.5, 3.8, 3. , 3.8, 3.2, 3.7, 3.3, 3.2, 3.2,
       3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7, 2. , 3. , 2.2, 2.9, 2.9,
       3.1, 3. , 2.7, 2.2, 2.5, 3.2, 2.8, 2.5, 2.8, 2.9, 3. , 2.8, 3. ,
       2.9, 2.6, 2.4, 2.4, 2.7, 2.7, 3. , 3.4, 3.1, 2.3, 3. , 2.5, 2.6,
       3. , 2.6, 2.3, 2.7, 3. , 2.9, 2.9, 2.5, 2.8, 3.3, 2.7, 3. , 2.9,
       3. , 3. , 2.5, 2.9, 2.5, 3.6, 3.2, 2.7, 3. , 2.5, 2.8, 3.2, 3. ,
       3.8, 2.6, 2.2, 3.2, 2.8, 2.8, 2.7, 3.3, 3.2, 2.8, 3. , 2.8, 3. ,
       2.8, 3.8, 2.8, 2.8, 2.6, 3. , 3.4, 3.1, 3. , 3.1, 3.1, 3.1, 2.7,
       3.2, 3.3, 3. , 2.5, 3. , 3.4, 3. ]

print('RATINGS 1', stats.shapiro(ratings_1))
print('RATINGS 2', stats.shapiro(ratings_2))
#обе выборки не отвергают гипотезу нормальности

print(stats.ttest_ind(ratings_1, ratings_2, alternative = 'greater', equal_var = False))
#Вывод - из-за уровня значимости отвергаем гипотезу об отсутствии консервативности в пользу её присутствия 