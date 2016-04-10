import math
myresult = open('result.txt', 'a')
covarianceMatrix = [[0.0005,0.00008,0.00005,0.00006,0.00009,0.0001,0.0001,0.0001],[0.00008,0.0149,0.00006,-0.0002,0.0002,0.0001,0.0006,-0.0003],[0.00005,0.00006,0.0002,0.00002,0.0001,0.0001,0.0001,0.00008],[0.00006,-0.0002,0.00002,0.0004,0.00001,0.00009,0.00008,0.00006],[0.00009,0.0002,0.0001,0.00001,0.0002,0.0002,0.0002,0.00006],[0.0001,0.0001,0.0001,0.00009,0.0002,0.0005,0.0003,0.0001],[0.0001,0.0006,0.0001,0.00008,0.0002,0.0003,0.0009,0.0001],[0.0001,-0.0003,0.00008,0.00006,0.00006,0.0001,0.0001,0.0004]]
for one in range(0, 101, 10):
	for two in range(0, 101, 1):
		for three in range(0, 101, 1):
			for four in range(0, 101, 1):
				for five in range(0, 101, 1):
					for six in range(0, 101, 1):
						for seven in range(0, 101, 1):
							for eight in range(0, 101, 1):
								if one+two+three+four+five+six+seven+eight==100:
									mylist = [one/100, two/100, three/100, four/100, five/100, six/100, seven/100, eight/100]
									myStringList = str(mylist)
									companyName = ['Alibaba','Arch Coal', 'IBM', 'Bank of China', 'Exxon', 'PetroChina', 'Gazprom', 'Palo Alto Networks']
									averageReturn = [- 0.12, - 0.84, - 0.06, 0.02, - 0.05, - 0.14, - 0.11, 0.17]
									averageVolatility = [2.12, 12.16, 1.35, 1.96, 1.40, 2.14, 3.04, 2.04]
									portfolioR = mylist[0]*averageReturn[0]+mylist[1]*averageReturn[1]+mylist[2]*averageReturn[2]+mylist[3]*averageReturn[3]+mylist[4]*averageReturn[4]+mylist[5]*averageReturn[5]+mylist[6]*averageReturn[6]+mylist[7]*averageReturn[7]
									# ##############################
									subsum = 0
									for r in range(8):
										for c in range(8):
											sub=mylist[r]*mylist[c]*covarianceMatrix[r][c]
											subsum += sub
									portfolioV= math.sqrt(subsum)

									#################################
									mystringR = str(portfolioR)
									mystringV = str(portfolioV)
									myresult.write(myStringList+";"+mystringR+";"+mystringV+"\n")
myresult.close()