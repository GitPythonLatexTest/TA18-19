import numpy as np
import matplotlib.pyplot as plt


data = [[66, 27, 75, 57, 32],
		[54, 44, 22, 12, 32],
		[22, 55, 34, 23, 87],
		[45, 454, 22, 22, 12],
		[23, 84, 88, 92, 12]]

columns = ('Case id', 'activity', 'Quality', 'High', 'Cost')
rows = ['%d Tahun' % x for x in (2022, 2021, 2020, 2019, 2018)]

values = np.arange(0, 2500, 500)
value_increment = 1000

colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
n_rows = len(data)

index =np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offeset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
	plt.bar(index, data[row], bar_width, bottom=y_offeset, color=colors[row])
	y_offeset = y_offeset + data[row]
	cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offeset])

colors =colors[::-1]
cell_text.reverse()

the_table = plt.table(cellText=cell_text,
								rowLabels=rows,
								rowColours=colors,
								colLabels=columns,
								loc='bottom')

plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Strategi Pengadaan Pendapatan Rp.{0}".format(value_increment))
plt.yticks(values * value_increment, ['%d'% val for val in values])
plt.xticks([])
plt.title('Data Procuretment Of Goods Service')

plt.show()