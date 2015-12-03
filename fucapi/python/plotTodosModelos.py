import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

#modelos SMO
plt.plot(0.346,0.863, 'gD')
plt.plot(0.218,0.885, 'gD')
plt.plot(0.207,0.896, 'gD')
plt.plot(0.199,0.895, 'gD')
plt.plot(0.169,0.891, 'gD')

#modelos J48
plt.plot(0.701,0.867, 'bD')
plt.plot(0.328,0.862, 'bD')
plt.plot(0.335,0.866, 'bD')
plt.plot(0.324,0.859, 'bD')
plt.plot(0.287,0.853, 'bD')

#modelos REPTree
plt.plot(0.815,0.840, 'cD')
plt.plot(0.497,0.797, 'cD')
plt.plot(0.507,0.807, 'cD')
plt.plot(0.499,0.796, 'cD')
plt.plot(0.431,0.777, 'cD')

#modelos RandomTree
plt.plot(0.623,0.821, 'yD')
plt.plot(0.408,0.773, 'yD')
plt.plot(0.435,0.789, 'yD')
plt.plot(0.426,0.780, 'yD')
plt.plot(0.377,0.766, 'yD')

#modelos NaiveBayes
plt.plot(0.619,0.836, 'mD')
plt.plot(0.420,0.768, 'mD')
plt.plot(0.448,0.762, 'mD')
plt.plot(0.417,0.747, 'mD')
plt.plot(0.319,0.709, 'mD')



#Baseline ZeroR
plt.plot(0.842,0.842, 'rD')
#ax.annotate('A', xy=(0.850,0.842), textcoords='offset points')
plt.plot(0.757,0.757, 'rD')
#ax.annotate('B', xy=(0.765,0.757), textcoords='offset points')
plt.plot(0.769,0.769, 'rD')
plt.plot(0.760,0.760, 'rD')
plt.plot(0.722,0.722, 'rD')
plt.plot([0,1],'r-')


plt.title('Grafico ROC')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])

#plt.annotate('pior modelo', xy=(0.842,0.842), yxtext=(0.8, 0.4), arrowprops=dict(facecolor='black',shrink=0.05))

plt.show()