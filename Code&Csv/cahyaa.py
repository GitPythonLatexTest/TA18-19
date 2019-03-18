import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('cahya1.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(str(row[0]))
		y.append(int(row[1]))

plt.plot(x,y, label ='the result data')
plt.xlabel('desa')
plt.ylabel('jumlah data')
plt.title('the result data')
plt.legend()
plt.show()
