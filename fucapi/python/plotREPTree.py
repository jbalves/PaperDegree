import matplotlib.pyplot as plt

#x =[]
#y =[]

#dataset = open('resultExperimento01.csv', 'r') 

#for line in dataset:
#	line = line.strip() #23,24\n -> 23,34
#	X, Y = line.split(',')
#	x.append(X)
#	y.append(Y)

#dataset.close()

#plt.plot(x,y,'bo')

plt.plot(0.815,0.840, 'rD')
plt.plot(0.497,0.797, 'bD')
plt.plot(0.507,0.807, 'gD')
plt.plot(0.499,0.796, 'cD')
plt.plot(0.431,0.777, 'mD')
plt.plot([0,1],'r-')
#plt.legend(loc='upper left')

plt.title('Algoritmo REPTree')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])


plt.show()
