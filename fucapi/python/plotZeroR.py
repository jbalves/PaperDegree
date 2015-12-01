import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(0.842,0.842, 'rD')
ax.annotate('A', xy=(0.850,0.842), textcoords='offset points')
plt.plot(0.757,0.757, 'bD')
ax.annotate('B', xy=(0.765,0.757), textcoords='offset points')
plt.plot(0.769,0.769, 'gD')
plt.plot(0.760,0.760, 'cD')
plt.plot(0.722,0.722, 'mD')
plt.plot([0,1],'r-')


plt.title('Algoritmo ZeroR')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])

#plt.annotate('pior modelo', xy=(0.842,0.842), yxtext=(0.8, 0.4), arrowprops=dict(facecolor='black',shrink=0.05))

plt.show()