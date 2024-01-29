import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)



fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)


fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(122)
ax3 = fig.add_subplot(223)


fig = plt.figure(figsize = (14,5))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(122)
ax3 = fig.add_subplot(223)

f = ax1.hist(randn(100), bins = 20, color = 'y', alpha = 0.5)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
ax3.plot(randn(100).cumsum(), 'k--')

plt.show()
plt.close()

plt.plot(randn(100).cumsum())
plt.show()

fig, axes = plt.subplots(2, 3)
fig.set_figheight(5)
fig.set_figwidth(15)

axes[0, 1].scatter(np.arange(30), np.arange(30) + 3 * randn(30))
axes[1, 1].bar(np.arange(10), randn(10))

plt.show()

fig, axes = plt.subplots(2, 2, sharex= True, sharey= True)
fig.set_figheight(5)
fig.set_figwidth(15)

for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins = 50, color = 'g', alpha = 0.5 )

plt.subplots_adjust(wspace = 0.0, hspace = 0.0)

plt.show()

fig, axes = plt.subplots(2, 2, sharex= False, sharey= True)
fig.set_figheight(5)
fig.set_figwidth(15)

for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins = 50, color = 'g', alpha = 0.5 )

plt.subplots_adjust(wspace = 0.2, hspace = 0.2)
plt.savefig('fig.png', dpi = 400, bbox_inches = 'tight')

plt.show()



