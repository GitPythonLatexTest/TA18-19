import matplotlib.pyplot as plt
import numpy as np
x,y = np.genfromtxt('E:\\University\\climate.csv', unpack=True, delimiter=',')
plt.plot(x,y)
plt.xlabel('Day'),
plt.ylabel('Air Temperature'),
plt.show()