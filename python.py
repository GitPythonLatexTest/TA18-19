import matplotlib.pyplot as faisal
import csv

x = []
y = []

with open('data.csv','r') as faisalcsvfile:
    plots = csv.reader(faisalcsvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(int(row[1]))

faisal.plot(x,y, label='Loaded from file!')
faisal.xlabel('Jenis Barang')
faisal.ylabel('Jumlah Barang')
faisal.title('Graph Purchase Order')
faisal.legend()
faisal.show()