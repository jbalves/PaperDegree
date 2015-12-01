import matplotlib.pyplot as plt

plt.plot(0.619,0.836, 'rD')
plt.plot(0.420,0.768, 'bD')
plt.plot(0.448,0.762, 'gD')
plt.plot(0.417,0.747, 'cD')
plt.plot(0.319,0.709, 'mD')
plt.plot([0,1],'r-')

plt.title('Algoritmo NaiveBayes')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])


plt.show()