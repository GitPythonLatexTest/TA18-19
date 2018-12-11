import matplotlib.pyplot as ikhsan
import csv

x = []
y = []

with open('ikhsan.csv', 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter=',')
  for row in plots:
    x.append(str(row[0]))
    y.append(int(row[1]))

ikhsan.plot(x,y, label='Loaded from file')
ikhsan.xlabel('Total Value')
ikhsan.ylabel('Total Weight')
ikhsan.title('Knapsack Problem')
ikhsan.legend()
ikhsan.show()
