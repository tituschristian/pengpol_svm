
selectedKernel = 0
degree = 2
constanta = 1
thou = 0
lamda = 3
gamma = 0.05

# Data
banyakFitur = 2
banyakData = 4
'''arrayData = [
  [60,  165],
  [70,  160],
  [80,  165],
  [100, 155],
  [40,  175]]'''
arrayData = [
  [1,    1],
  [1,   -1],
  [-1,   1],
  [-1,  -1]]
'''arrayKelas = [
  1, 1, 1, -1, -1
]'''
arrayKelas = [
  -1, 1, 1, -1
]
arrayD = []
arrayK = []

def setDegree():
	global degree
	degree = int(input("Input degree: "))

def setConstanta():
	global constanta
	while True:
		constanta = int(input("Input constanta: "))
		if constanta < 1:
			print("Masukkan constanta lebih dari 1")
		else:
			break

def setLamda():
	global lamda
	lamda = int(input("Input lambda: "))

def setGamma():
	global gamma
	gamma = float(input("Input gamma: "))

def setArrayData():
	global arrayData
	global banyakData
	global banyakFitur
	banyakFitur = int(input("Masukkan banyak fitur: "))
	banyakData = int(input("Masukkan banyak data: "))
	print("Silahkan masukkan data setiap baris")

	for i in range(banyakData):
		print("Fitur ", (i+1), end='|')

	print("Kelas / Kategori")
	for i in range(banyakData):
		row = [int(x) for x in input().split()]
		arrayData.append(row)

def printArrayData():
	for i in range(len(arrayData)):
		for j in range(len(arrayData[i])):
			print(arrayData[i][j], end=' ')
		print("")
	print("")

def printArrayD():
	for i in range(len(arrayD)):
		for j in range(len(arrayD[i])):
			print(arrayD[i][j], end=' ')
		print("")
	print("")

def linier(x, y):
	result = 0
	for i in range(len(x)):
		result += x[i] * y[i]
	return result
			
def polinomialDegreeD(x, y):
	if(degree == 0):
		setDegree()
	
	result = 0
	for i in range(len(x)):
		result += x[i] * y[i]
	result = result ** degree
	return result
	
def polinomialDegreeUpToD(x, y):
	if (degree == 0):
		setDegree()
	if (constanta < 1):
		setConstanta()
	
	result = 0
	for i in range(len(x)):
		result += x[i] * y[i]
		#print(result, "->", end='')
	result = result + constanta
	#print("result plus constanta", result)
	result = result ** degree
	#print("result ", result)
	return result

'''
def setSelectedKernel():
	print("1. Linier")
	print("2. Polinomial of Degree D")
	print("3. Polinomial of Degree up to D")
	print("4. Gaussian RBF")
	print("5. Sigmoid")
	print("6. Invers Multi Kuadratik")
	print("7. Additive")
	selectedKernel = input("Select Kernel: ")

def calculateKernel()
	if (selectedKernel == 0):
		print("Please select kernel")
		setSelectedKernel()
	else:
'''		

def calculateArrayD():
	global arrayD
	for i in range(banyakData):
		row = []
		for j in range(banyakData):
			#print("data yang digunakan ", arrayData[i], "dan ", arrayData[j])
			row.append( arrayKelas[i] * arrayKelas[j] 
			* ( polinomialDegreeUpToD(arrayData[i], arrayData[j]) + (lamda**2) ))
		print(row)
		arrayD.append(row)


def seqLearning():
	ai = [0.0 for i in range(banyakData)]
	calculateArrayD()
	dAi = [0.0 for i in range(banyakData)]
	newAi = [0.0 for i in range(banyakData)]
	while True:
		ei = [0.0 for i in range(banyakData)]
		for i in range(banyakData):
			#print(ei[i] , "===>")
			for j in range(banyakData):
				#print(ai[i] , )
				ei[i] += (ai[j] * arrayD[i][j])
				#print(ai[i], "*", arrayD[i][j], "=", ei[i] , "-> ", end='')
			#print("Ei %.6f" %ei[i])
			dAi[i] = min( max(gamma * (1 - ei[i]), -1 * ai[i] ), (constanta - ai[i]) )
			#print("delta Ai %.6f" %dAi[i])
			newAi[i] = ai[i] + dAi[i]
			#print("new Ai %.6f" %newAi[i])
		
		#print("cek")
		count = 0
		for i in range(banyakData):
			if dAi[i] <= 0.00001:
				count += 1
			ai[i] = newAi[i]
		
		if count == banyakData:
			break
	
	for i in range(len(ai)):
		print("alpha ", (i+1), "= %.3f" %ai[i])
		
	return ai

	
#print(linier( [2], [2] ) )
#setArrayData()
printArrayData()
seqLearning()
#calculateArrayD()
#printArrayD()