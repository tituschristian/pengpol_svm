
selectedKernel = 0
degree = 0
constanta = 0
thou = 0
lamda = 0

# Data
banyakFitur = 0
banyakData = 0
arrayData = []
arrayD = []
arrayK = []

def setDegree():
	global degree
	degree = int(input("Input degree: "))
	
def setConstanta():
	global constanta
	constanta = int(input("Input constanta: "))

def setLamda():
	global lamda
	lamda = int(input("Input lambda: "))

def setArrayData():
	global arrayData
	global banyakData
	global banyakFitur
	banyakFitur = int(input("Masukkan banyak fitur: "))
	banyakData = int(input("Masukkan banyak data: "))
	for i in range(banyakData):
		row = [int(x) for x in input().split()]
		arrayData.append(row)

def printArrayData():
	for i in range(len(arrayData)):
		for j in range(len(arrayData[i])):
			print(arrayData[i][j], " ", end='')
		print("")
	print("")

def linier(x, y):
	result = 0
	for i in range(len(x)):
		result = x[i] * y[i]
	return result
			
def polinomialDegreeD(x, y):
	if(degree == 0):
		setDegree()
	
	result = 0
	for i in range(len(x)):
		result = x[i] * y[i]
	return result
	
def polinomialDegreeUpToD(x, y):
	if (degree == 0):
		setDegree()
	if (constanta == 0):
		setConstanta()
	
	result = 0
	for i in range(len(x)):
		result = x[i] * y[i]
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

def seqLearning():
	ai = 0
	a = 0
	return 0
	
#print(linier( [2], [2] ) )
setArrayData()
printArrayData()