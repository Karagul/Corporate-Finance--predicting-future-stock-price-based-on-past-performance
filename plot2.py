import matplotlib.pyplot as plt

myfile = open('result.txt', 'r')
averageReturn = []
averageVolatility = []
weight = []
for line in myfile:
	string = line.strip()
	templist = string.split(';')
	averageReturn.append(float(templist[1]))
	averageVolatility.append(float(templist[2]))
	weight.append(templist[0])

plt.ylabel("Expected Return: %")
plt.xlabel('Volatility')
plt.scatter(averageVolatility, averageReturn)
plt.show()
myfile.close()