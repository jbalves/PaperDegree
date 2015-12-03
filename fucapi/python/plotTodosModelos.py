import matplotlib.pyplot as plt
import numpy as np


def ler_base_dados(arquivo):
	x = []
	y = []

	dataset = open(arquivo, 'r')

	for line in dataset:
		line = line.strip()
		X,Y = line.split(',')
		x.append(X)
		y.append(Y)

	dataset.close()
	
	return x,y	

fig = plt.figure()

x1, y1 = ler_base_dados('dataSMO.csv')
x2, y2 = ler_base_dados('dataJ48.csv')
x3, y3 = ler_base_dados('dataREPTree.csv')
x4, y4 = ler_base_dados('dataRandomTree.csv')
x5, y5 = ler_base_dados('dataNaiveBayes.csv')
x6, y6 = ler_base_dados('dataZeroR.csv')


ax1 = fig.add_subplot(111)
#ax.plot(0.346,0.863, 'gD', label='SMO')
ax1.plot(x1,y1,'gD', label='SMO')
ax1.plot(x2,y2,'bD', label='J48')
ax1.plot(x3,y3,'cD', label='REPTree')
ax1.plot(x4,y4,'yD', label='RandomTree')
ax1.plot(x5,y5,'mD', label='NaiveBayes')
ax1.plot(x6,y6,'rD', label='ZeroR')
ax1.plot([0,1],'r--')

ax1.legend(loc='lower right', numpoints=1, fontsize=12)
#ax1.legend(loc="lower left", numpoints=1, fontsize=10)
#scatterpoints=1

#modelos SMO
#plt.plot(0.346,0.863, 'gD', label='SMO')
#plt.plot(0.218,0.885, 'gD')
#plt.plot(0.207,0.896, 'gD')
#plt.plot(0.199,0.895, 'gD')
#plt.plot(0.169,0.891, 'gD')

#modelos J48
#plt.plot(0.701,0.867, 'bD')
#plt.plot(0.328,0.862, 'bD')
#plt.plot(0.335,0.866, 'bD')
#plt.plot(0.324,0.859, 'bD')
#plt.plot(0.287,0.853, 'bD')

#modelos REPTree
#plt.plot(0.815,0.840, 'cD')
#plt.plot(0.497,0.797, 'cD')
#plt.plot(0.507,0.807, 'cD')
#plt.plot(0.499,0.796, 'cD')
#plt.plot(0.431,0.777, 'cD')

#modelos RandomTree
#plt.plot(0.623,0.821, 'yD')
#plt.plot(0.408,0.773, 'yD')
#plt.plot(0.435,0.789, 'yD')
#plt.plot(0.426,0.780, 'yD')
#plt.plot(0.377,0.766, 'yD')

#modelos NaiveBayes
#plt.plot(0.619,0.836, 'mD')
#plt.plot(0.420,0.768, 'mD')
#plt.plot(0.448,0.762, 'mD')
#plt.plot(0.417,0.747, 'mD')
#plt.plot(0.319,0.709, 'mD')



#Baseline ZeroR
#plt.plot(0.842,0.842, 'rD')
#ax.annotate('A', xy=(0.850,0.842), textcoords='offset points')
#plt.plot(0.757,0.757, 'rD')
#ax.annotate('B', xy=(0.765,0.757), textcoords='offset points')
#plt.plot(0.769,0.769, 'rD')
#plt.plot(0.760,0.760, 'rD')
#plt.plot(0.722,0.722, 'rD')
#plt.plot([0,1],'r-')


#plt.title('Grafico ROC')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])

#plt.annotate('pior modelo', xy=(0.842,0.842), yxtext=(0.8, 0.4), arrowprops=dict(facecolor='black',shrink=0.05))

plt.show()