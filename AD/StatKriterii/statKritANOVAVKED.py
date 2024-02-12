import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd
from IPython.display import *
from tqdm.notebook import tqdm

np.random.seed(3106)

#задача по вычислению является ли велика разница между транспортными средствами для курьеров
distrib = stats.norm(loc = 35, scale = 10)
gen_pop = distrib.rvs(size = 10000)

fig = plt.figure(figsize= (14,7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 100)
plt.show()

#извлекаем 3 случ совокупности по 50 заказов в каждой
sample_groups = []
for i in range(3):
    sample_groups.append(np.random.choice(gen_pop, size = 50).astype(int))
sample_groups = np.array(sample_groups)
print(sample_groups)

#рассчитано - среднее каждой выборки и станд отклонение(голубые линии)
#среднее средних и стандартное отклонение средних (оранжевая линия)

x = np.mean(sample_groups, axis = 1)
y = np.arange(sample_groups.shape[0])
e = np.std(sample_groups, axis = 1)

fig = plt.figure(figsize = (14, 7))
plt.errorbar(x, y, xerr = e, linestyle = 'None', 
             marker = 'o')
plt.errorbar(np.mean(x), y.shape[0], 
             xerr = np.std(x), linestyle = 'None', 
             marker = 'o' )

plt.show()

#   1)Формулируется гипотезы H0 и H1
#H0 - выборки взяты из одного распр (среднее всех выборок равны)
#H1 - выборки взяты из разных распределений (хот ябы пара средних различается между собой)
#   2) Фиксируется уроввень занчимости критерия значимости
#Зададим альфа на уровне значимости 5%
#   3) Выбирается статистически ритерий для проверки гипотезы
#Будем использовать ANOVA
#   4) По выборочным данным вычисляется значение К-наблюдаемое по распределению выбранной статистики

num_of_groups = sample_groups.shape[0]
#среднее по всем наблюдениям
x_mean = sample_groups.mean()
print('среднее по всем наблюдениям ', x_mean)

#среднее для каждой группы
group_means = sample_groups.mean(axis = 1)
group_means_reshaped = group_means.reshape(num_of_groups, 1)

#SSW - сумма средних квадратичных отклонений
SSW = np.sum((sample_groups - group_means_reshaped) ** 2)
print('SSW ', SSW)

#SSB - суммы отклонений груповых средних от среднего всей совокупности данных
group_lengths = [x.shape[0] for x in sample_groups]
SSB = np.sum((group_means - x_mean)** 2 * group_lengths)
print('SSB ', SSB)

#F - статистика критериев фишера
m = num_of_groups
N = np.sum(group_lengths)

F = (SSB / (m-1)) / (SSW / (N - m))
print('F ', F)

F, p = stats.f_oneway(*sample_groups)
print('F ', F)

#дисперсионный анализ - статистическая процедура для сравнения
#   5) С учетом выбранного уровян значимости вычисляется критическая область
#и область принятия гипотезы, то есть К - критическое

#F критическое
F_critical = stats.f.ppf(q = 1 - .05, dfn = m, dfd = N - m)
print('F критическое ', F_critical)

#   6) найденое значение К-наблюдаемое критерия сравнивается с К-критическим -  здесь F - F_CRITICAL - ФИШЕРА
#и по результатам сравнения делается вывод
print('Не можем отвергнуть гипотезу H0') if F < F_critical else print('H0 отвергается')
print('P значение', p) #Вероятность отвергнуть гипотезу, достигаемый уровень значимости
#Вероятность получить такие или ещё более сильные различия между нашими группами при условии что различий нет
print(p > 0.05) #Не можем отвергнуть гипотезу H0 ибо True

#разбираемся с распределением F - извлекаем из ген совокупности выборки и считаем F
def calculate_random_sample_group(sz=50, num_of_groups=3, gen_pop=np.random.normal(size=1000)):
    sample_groups = []
    for i in range(num_of_groups):
        sample_groups.append(np.random.choice(gen_pop, size=sz))
    F, _ = stats.f_oneway(*sample_groups)
    return sample_groups, F

Fs = []
sgs = []
for i in tqdm(range(10000)):
    sg, F = calculate_random_sample_group()
    Fs.append(F)
    sgs.append(sg)
#распределение приняло опр форму распределения Фишера по его статистикам принималиась решения
plt.figure(figsize=(10, 6))
plt.hist(Fs, bins=100)
plt.show()

#критерии согласия - критерии занимости применения для проверки гипотез
#о законе распределения генеральной совокупности, из которой взята выборка
#критерии для проверки стат гипотезы
#Шапиро-Уилки, Хи-квадрат, Колмогорова-Смирнова критерии

#Параметрические критерии - критерии значимости,
#которые служат для проверки гипотез о параметрах рапределений
#t- критерий Стьюдента(связанные выборки и независимые выборки)
#F - критерий Фишера(независимые выборки)

#Непараметрический критерий - критерий значимости, который для проверки
#статистических гипотез не использует предположений о распределении
#генеральной совокупности
#критерий Манна-Уитни, критерий Вилкоксона

#Парам и непарам критерии подразделяются на также:
#1) одновыборочные, 2)двувыборочные со связанными выборками
#3)результатами повторных измерений, вып в одном и том же множестве элементов
#4)двувыборочные с несвязанными выборками - элементы выборок
#не являются парными результатами повторных измерений, выполненных
#в одном и том же множестве элементов
