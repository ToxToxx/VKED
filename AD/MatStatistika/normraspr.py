import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd

import matplotlib.animation as animation
from wand.image import Image
from wand.display import display

np.random.seed(1234)

#Норм распределение(распр гауса) - самое частое распределение
#средние меридианы у того распределения совпадают
#задается средним и стандартным отклонением
#правило 3 сигм - вероятность что случ величина отклонится от своего мат ожидание
#на большую величину, чем 3 сигмы стремится к нулю

#при генерации n выборок из ген совокупности средняя выборка
#Конццентрируется вокруг среднего генеральной совокупности

#Центральная предельная теорема
#логнормальное распределение
ln_distrib = stats.lognorm(0.5, loc = 25, scale = 10)
gen_pop_ln = ln_distrib.rvs(size = 10000)

fig = plt.figure(figsize = (14, 7))
ax1 = plt.subplot(111)
plt.hist(gen_pop_ln, 100)
plt.show()

#Будем генерировать из него выборки размером 20, считать среднее
n = 20
avg = []
for i in range (1000):
    sample = np.random.choice(gen_pop_ln, n, replace = False)
    avg.append(np.mean(sample))

def clt(current):
    plt.cla()
    if current == 1000:
        a.event_source.stop()

    plt.hist(avg[0 : current], bins = 20)
    plt.annotate('Выборка = {}'.format(current), [3, 27])

fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval = 10)
plt.show()
#с увеличением итерация среднее по выборкам начинает концентрироваться в одном месте

#Предельная теорема - выборочные средние имеют приближенно
#норм распр независимо от расп исх совокупности из которой были извлечены выборки
#ср знач всех возможных выборочных средних равно среднему исх совокупности
#при этом станд отклонение всех возможных средних по выборкам данного объёма,
#называемое станд ошибкой среднего, зависит как от станд отклонения
#совокупности, так и от объёма выборки
#При этом:
#выборки должны извлекаться случайно;
#размер выборки не должен превышать 10% размера всей ген совокупности
#размер выборки должен быть достаточно большим

