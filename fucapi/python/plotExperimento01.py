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

plt.plot(x,y)

plt.title('Example')
plt.xlabel('x label')
plt.ylabel('y label')

plt.show()
