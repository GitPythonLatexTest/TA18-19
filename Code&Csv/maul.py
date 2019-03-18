import matplotlib.pyplot as maul
import csv

x = []
y = []

with open('maul.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(int(row[1]))

maul.plot(x,y, label='Loaded from file!')
maul.xlabel('True False Location')
maul.ylabel('The amount of goods')
maul.title('Graph Purchase Order')
maul.legend()
maul.show()
