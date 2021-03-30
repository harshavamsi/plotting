import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("P1T1.csv", 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[1])
        y.append(row[4])


plt.plot(x, y, marker='o')

plt.title('Title of the plot')

plt.xlabel('X axis label')
plt.ylabel('Y axis label')

plt.show()
