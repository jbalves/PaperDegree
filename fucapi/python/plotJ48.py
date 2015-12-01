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

plt.plot(0.701,0.867, 'rD')
plt.plot(0.328,0.862, 'bD')
plt.plot(0.335,0.866, 'gD')
plt.plot(0.324,0.859, 'cD')
plt.plot(0.287,0.853, 'mD')
plt.plot([0,1],'r-')
#plt.legend(loc='upper left')

plt.title('Algoritmo J48')
plt.xlabel('FP Rate')
plt.ylabel('TP Rate')
plt.axis([0,1,0,1])


plt.show()
