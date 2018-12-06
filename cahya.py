import matplotlib.pyplot as plt
import numpy as np
x,y = np.genfromtxt('E:\INTERNSHIP\python\desaa.csv', unpack=True, delimiter=',')
plt.plot(x,y)
plt.xlabel('desa')
plt.ylabel('jumlah data')
plt.show()