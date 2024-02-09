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