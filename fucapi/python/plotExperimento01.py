import matplotlib.pyplot as plt

x =[]
y =[]

dataset = open('resultExperimento01.csv', 'r') 

for line in dataset:
	line = line.strip() #23,24\n -> 23,34
	X, Y = line.split(',')
	x.append(X)
	y.append(Y)

dataset.close()

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('blue')

#plt.plot(x,y)

#plt.title('Example')
#plt.xlabel('FP Rate')
#plt.ylabel('TP Rate')

ax1 = fig.add_subplot(1,1,1,)


plt.show()
