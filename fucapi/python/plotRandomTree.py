import matplotlib.pyplot as plt

plt.plot(0.623,0.821, 'rD')
plt.plot(0.408,0.773, 'bD')
plt.plot(0.435,0.789, 'gD')
plt.plot(0.426,0.780, 'cD')
plt.plot(0.377,0.766, 'mD')
plt.plot([0,1],'r-')

plt.title('Algoritmo RandomTree')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])


plt.show()
