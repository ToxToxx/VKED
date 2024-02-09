import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd
from IPython.display import *

#задача по вычислению является ли велика разница между транспортными средствами для курьеров
distrib = stats.norm(loc = 35, scale = 10)
gen_pop = distrib.rvs(size = 10000)

fig = plt.figure(figsize= (14,7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 100)
plt.show()

#извлекаем 3 случ совокупности по 50 заказов в каждой
np.random.seed(3106)
sample_groups = []
for i in range(3):
    sample_groups.append(np.random.choice(gen_pop, size = 50).astype(int))
sample_groups = np.array(sample_groups)
print(sample_groups)