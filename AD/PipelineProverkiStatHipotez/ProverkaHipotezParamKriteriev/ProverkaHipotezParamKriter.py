from scipy import stats
from sklearn import datasets
from sklearn.utils import resample
from statsmodels.stats.weightstats import ztest as ztest
from statsmodels.stats.proportion import proportions_ztest
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

print('Критерий Уэлча', stats.ttest_ind(ratings_1, ratings_2, alternative = 'greater', equal_var = False))
#проверяем что среднее больше чем во второй
#Вывод - из-за уровня значимости отвергаем гипотезу об отсутствии консервативности в пользу её присутствия 


#СВЯЗАННЫЕ КРИТЕРИИ С МАЛЫМ ЧИСЛОМ НАБЛЮДЕНИЙ
#каждое наблюдение в паре или зависит от другого наблюдения другой выборки

sample_1 = [32.8, 44.3, 29. , 23.5, 26.7, 39. , 36.2, 25.6, 37.9, 36.5, 43.8,
       59.7, 37.7, 38.4, 32.1, 28.2, 34.4, 22.1, 12.6, 26.9, 29.9, 55.5,
       34.1, 22.4, 25.4, 40. , 22.5, 38.8, 43.6, 34.4]
sample_2 = [34.2, 35.4, 53.2, 37.8, 34.6, 31.4, 35.8, 40.4, 32.4, 29.8, 30.9,
       52.5, 44. , 32.3, 39.3, 31.7, 48.3, 34.7, 41.1, 52.3, 38.8, 55.8,
       35.4, 32.3, 31.4, 37.6, 33.3, 42.9, 48.9, 39.2]
alternative= 'two-sided'

print('Z статистика', stats.ttest_rel(sample_1,  sample_2, alternative = alternative))
#отвергаем нашу 0 гипотезу о равенстве средних

#БУТСТРАП
#универсальное решение для проверки гипотезы
#идея чтобы использовать результаты вычислений по выборкам 
#как фиктвную популяцию, делается для того чтобы определить
#выборочное распределение статистики при этмо фактически
#анализируется множество фантомных выборок - бутстрапов
#формируются выборки методом с возвращением
#мы не получаем в бутстрапе новой информации
#но разумно используем имеющиеся исходя из задачи
#ограничение: выборка должна быть похожа с генеральной совокупностью

#ЗАДАЧА НА ПРОВЕРКУ 90 ПРОЦЕНТИЛЯ И РЕШЕНИЯ КАКОЙ АЛГОРИТМ ЛУЧШЕ НОВЫЙ ИЛИ СТАРЫЙ
#ГИПОТЕЗА НУЛЕВАЯ ЧТО ОНИ ОДИНАКОВЫ
ln_distrib = stats.lognorm(0.5, loc = 20, scale = 7)
old_version = ln_distrib.rvs(size=1000)

ln_distrib = stats.lognorm(0.5, loc = 17, scale = 8.3)
new_version = ln_distrib.rvs(size=1000)

fig = plt.figure(figsize=(14, 3))
ax1 = plt.subplot(121)
plt.hist(old_version, 100, alpha=0.8)
plt.title('Распределение времени работы старого алгоритма')

ax1 = plt.subplot(122)
plt.hist(new_version, 100, alpha=0.8, color = 'r')
plt.title('Распределение времени работы нового алгоритма')

plt.show()

#РЕШЕНИЕ
old_version_90p_boostrap_distribution = []
new_version_90p_boostrap_distribution = []

for i in range(1000):
    sample_old_version = resample(old_version, replace=True, n_samples=100, random_state=i)
    sample_new_version = resample(new_version, replace=True, n_samples=100, random_state=i)
    
    old_version_90p_boostrap_distribution.append(np.percentile(sample_old_version, 90))
    new_version_90p_boostrap_distribution.append(np.percentile(sample_new_version, 90))

fig = plt.figure(figsize=(14, 3))
ax1 = plt.subplot(121)
plt.hist(old_version_90p_boostrap_distribution, 100, alpha=0.8)

ax1 = plt.subplot(122)
plt.hist(new_version_90p_boostrap_distribution, 100, alpha=0.8, color = 'r')

plt.show()

t, p = stats.ttest_ind(old_version_90p_boostrap_distribution,
                        new_version_90p_boostrap_distribution,
                        alternative='greater')

print(f't: {t}, p: {p}')
#p слишком мало - отвергаем гипотезу в пользу альтернативной

#ОЦЕНКА ДОЛЕЙ
#ГИПОТЕЗА ДОЛЯ РАВНЯЕТСЯ p - является ли конверсия случайной или нет
#одновыб критерий с большим числ набл
count = np.array(100)
nobs = np.array(300)
value = 0.5
print('Стистика доли', proportions_ztest(count, nobs, value = value))
#отвергаем в пользу альтернативной - посещений клиентво не случайный

#двувыборочный критерий с большим числом набл незав выборок
#имеется распр Бернули
#Гипотеза о равенстве долей
count = np.array([100, 400])
nobs = np.array([300, 800])
print('Статистика о равенстве долей', proportions_ztest(count, nobs, alternative='smaller'))
#отвергаем в пользу альтернативной

#ЗАДАЧА ОБ ОПЫТЕ ПРИЛОЖЕНИЯ ДОСТАВКИ ЕДЫ
#ГИПОТЕЗА О ТОМ ЧТО ПРОМОКДЫ УВЕЛИЧИВАЮТ ПОЛОЖ ОПЫТ ОТ ИСП ДОСТАВКИ
survey_1 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1,
       1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0,
       0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0,
       1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1,
       1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]
survey_2 = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0,
       1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1,
       0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1,
       0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0,
       1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]

def proportions_diff_z_stat_rel(sample1, sample2):
    sample = zip(sample1, sample2)
    n = len(sample1)
    
    f = sum([1 if (x[0] == 1 and x[1] == 0) else 0 for x in sample])
    g = sum([1 if (x[0] == 0 and x[1] == 1) else 0 for x in sample])
    
    return float(f - g) / np.sqrt(f + g - float((f - g)**2) / n )

def proportions_diff_z_test(z_stat, alternative = 'two-sided'):
    
    if alternative == 'two-sided':
        return z_stat, 2 * (1 - stats.norm.cdf(np.abs(z_stat)))
    
    if alternative == 'less':
        return z_stat, stats.norm.cdf(z_stat)

    if alternative == 'greater':
        return z_stat, 1 - stats.norm.cdf(z_stat)
    
    
print('Доли выборок', proportions_diff_z_test(proportions_diff_z_stat_rel(survey_1,survey_2),'less' ))
#Различаются доли в выборках