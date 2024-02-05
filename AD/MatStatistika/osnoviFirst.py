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
#генеральная совокупность данных
mean = np.mean(gen_pop)
print('Ср. арифм генеральное: ', mean)

#выборочная производим оценку по выборке
n = 20
sample = np.random.choice(gen_pop, n, replace = False)

sample_mean = np.mean(sample)
print('Ср ариф выборки: ', sample_mean)

#Меры разброса
#дисперсия - Разброс чего-либо и численная характеристика такого разброса
#среднеквадратичное отклонение - Наиболее распространённый показатель рассеивания значений случайной величины относительно её математического ожидания
#дисперсия
var_ = np.var(gen_pop)

#среднеквадратичное отклонение
std_ = np.std(gen_pop)

print('Дисперсия: ', var_, '\nСреднеквадратичное отклонение: ', std_)

#выборочное среднеквадратичное отклонение
std_sample = np.std(sample, ddof = 1) #деление на n-1 благодаря ddof
print('Выбороченое среднекв откл: ', std_sample)

iterations = 1000
n = 20

std_sample_l = []
std_sample_l_corrected = []

for i in range(iterations):
    sample = np.random.choice(gen_pop, n, replace = False)
    std_sample = np.std(sample)
    std_sample_corrected = np.std(sample, ddof = 1)    
    std_sample_l.append(std_sample)
    std_sample_l_corrected.append(std_sample_corrected)

fig = plt.figure(figsize = (15, 7))

ax1 = plt.subplot(111)
plt.hist(std_sample_l, alpha = 0.5, bins = 30)
plt.hist(std_sample_l_corrected, alpha = 0.5, bins = 30)

line1 = plt.axvline(std_, color = 'black', linestyle = 'dashed',
                    linewidth = 4.5, label = 'std генеральной совокупности')
line2 = plt.axvline(np.mean(std_sample_l), color = 'blue', linestyle = 'dashed',
                    linewidth = 4.5, label = 'std выборки')
line3 = plt.axvline(np.mean(std_sample_l_corrected), color = 'red', linestyle = 'dashed',
                    linewidth = 4.5, label = 'std выборки скорректированная')

plt.legend()
plt.show()

#СТАНДАРТНАЯ ОШИБКА СРЕДНЕГО - величина,
#характеризующая стандартное отклонение выбранного срденго,
#рассчитанное по выборке размера n из ген совокупности

n = 20
sample = np.random.choice(gen_pop, n, replace = False)
#оценка стандартной ошибки по выборке
print('Стандартная ошибка по выборке: ', stats.sem(sample))

fig = plt.figure(figsize = (10, 5))

ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha = 0.8)
line1 = plt.axvline(mean, label = ('Среднее =' + str(round(mean, 1))),
                    color = 'blue', linestyle = 'dashed', linewidth = 3.5, alpha = 0.4)
ax1.legend(handles = [line1], fontsize = 15)
plt.show()

n = 100
for i in range(5):
    sample = np.random.choice(gen_pop, n, replace = False)
    sample_mean = np.mean(sample)
    sem = stats.sem(sample)
    fig = plt.figure(figsize = (8, 4))
    ax1 = plt.subplot(111)
    plt.hist(sample, 20, alpha = 0.8)
    line1 = plt.axvline(sample_mean, label = ('Выборочное среднее: ' + str(round(sample_mean, 1))),
                        color = 'blue', linestyle = 'dashed', linewidth = 3, alpha = 0.4)
    line2 = plt.axvline(mean, label = ('Истинное среднее: ' + str(round(mean, 1))),
                        color = 'yellow', linestyle = 'dashed', linewidth = 3, alpha = 0.4)
    line3 = plt.axvline(sample_mean, label = ('Выборочная стандартная ошибка среднего: ' + str(round(sem, 1))),
                        color = 'red', linestyle = 'dashed', linewidth = 3, alpha = 0.0)
    ax1.legend(handles = [line1, line2, line3], fontsize = 10)
    plt.show()
#чем больше выборка - тем меньше стандартная ошибка

#оценка несмещена если её мат ожидание 
#равно истинному значению оцененному параметру
#асимптотическая несмещенность - более слабое услвоие,
#мат ожидание сходится с истинным занчением параметра
#с ростом объема выборки
iterations = 5000
n = 20

std_sample_l = []
std_sample_l_corrected = []

est = []
est_l = []

for i in range(iterations):
    sample = np.random.choice(gen_pop, n, replace = False)
    std_sample = np.std(sample)
    std_sample_corrected = np.std(sample, ddof = 1)
    std_sample_l.append(std_sample)
    std_sample_l_corrected.append(std_sample_corrected)
    if i%20 == 0:
        est.append(np.abs(np.mean(std_sample_l) - std_))
        est_l.append(np.abs(np.mean(std_sample_l_corrected) - std_))

fig = plt.figure(figsize = (12, 6))
plt.plot(est)
plt.plot(est_l)
plt.show() #с ростом числа наблюдений оценка наклонения становится всё точнее
#смешенная оценка становится всё больше и больше с точки зрения ошибки

#Состоятельность = рпи бесконечном расширении выборки
#оценка приходит к истинному значению
est = []
for i in range(10, 5000,10):
    sample = np.mean(np.random.choice(gen_pop, i, replace = False))
    est.append(sample)

plt.figure(figsize = (14, 8))
plt.plot(est, c = 'grey', alpha = 0.5)
plt.hlines(mean, 0, 500, color = 'blue', lw = 2, label = 'среднее генеральной совокупности')
plt.xlabel('количество наблюдений * 10', size = 12)
plt.legend()
plt.show()

#пример несостоятельной оценки
est = []
for i in range(10, 5000,10):
    sample = np.mean(np.random.choice(gen_pop, i, replace = False)) * (np.sqrt(i)/ i) * 30
    est.append(sample)

plt.figure(figsize = (14, 8))
plt.plot(est, c = 'grey', alpha = 0.5)
plt.hlines(mean, 0, 500, color = 'blue', lw = 2, label = 'среднее генеральной совокупности')
plt.xlabel('количество наблюдений * 10', size = 12)
plt.legend()
plt.show()

#Несмещенная оценка называется эффективной
#среди рассм. оценок, если она имеет минимальную дисперсию
