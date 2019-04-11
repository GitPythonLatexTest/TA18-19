import matplotlib.pyplot as achmad
import csv

x = []
y = []

with open('achmad.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(int(row[1]))

achmad.plot(x,y, label='Loaded from file!')
achmad.xlabel('Hari')
achmad.ylabel('Derajat Celcius')
achmad.title('Perkiraan Cuaca')
achmad.legend()
achmad.show()
