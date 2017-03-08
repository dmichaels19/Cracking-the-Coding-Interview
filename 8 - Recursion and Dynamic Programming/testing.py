import matplotlib.pyplot as plt
import sys

plotArray = []
size = 0
yaxis = 0
for line in sys.stdin:
    plotArray.append(line)
    size = size + 1
    yaxis = line

newy = round(float(yaxis),1)
plt.semilogy(range(size), plotArray, 'm')
plt.axis([0, 10, 0, newy+2])
plt.show()
