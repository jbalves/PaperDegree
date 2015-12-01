import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(0.346,0.863, 'rD')
ax.annotate('A', xy=(0.356,0.865), textcoords='offset points')
plt.plot(0.218,0.885, 'bD')
plt.plot(0.207,0.896, 'gD')
plt.plot(0.199,0.895, 'cD')
plt.plot(0.169,0.891, 'mD')
plt.plot([0,1],'r-')
#plt.legend(loc='upper left')

plt.title('Algoritmo SMO')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])


plt.show()
