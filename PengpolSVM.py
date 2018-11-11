
selectedKernel = 0
degree = 2
constanta = 2
thou = 0
lamda = 3
gamma = 0
maxGamma = 0

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
arrayAlphaI = []
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
	print("Masukkan gamma antara 0 - %.5f" %maxGamma)
	while True:
		gamma = float(input("Input gamma: "))
		if gamma <= 0 and gamma >= maxGamma:
			print("Masukkan gamma lebih dari 0 dan kurang dari %.5f" %maxGamma)
		else:
			break
	

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
	global maxGamma
	for i in range(banyakData):
		row = []
		for j in range(banyakData):
			#print("data yang digunakan ", arrayData[i], "dan ", arrayData[j])
			row.append( arrayKelas[i] * arrayKelas[j] 
			* ( polinomialDegreeUpToD(arrayData[i], arrayData[j]) + (lamda**2) ))
		print(row)
		arrayD.append(row)
	maxGamma = (2 / (max(max(arrayD))))

def seqLearning():
	global arrayAlphaI
	arrayAlphaI = [0.0 for i in range(banyakData)]
	calculateArrayD()
	setGamma()
	dAi = [0.0 for i in range(banyakData)]
	newAi = [0.0 for i in range(banyakData)]
	while True:
		ei = [0.0 for i in range(banyakData)]
		for i in range(banyakData):
			#print(ei[i] , "===>")
			for j in range(banyakData):
				#print(arrayAlphaI[i] , )
				ei[i] += (arrayAlphaI[j] * arrayD[i][j])
				#print(ai[i], "*", arrayD[i][j], "=", ei[i] , "-> ", end='')
			#print("Ei %.6f" %ei[i])
			dAi[i] = min( max(gamma * (1 - ei[i]), -1 * arrayAlphaI[i] ), (constanta - arrayAlphaI[i]) )
			#print("delta Ai %.6f" %dAi[i])
			newAi[i] = arrayAlphaI[i] + dAi[i]
			#print("new Ai %.6f" %newAi[i])
		
		#print("cek")
		count = 0
		for i in range(banyakData):
			if dAi[i] <= 0.00001:
				count += 1
			arrayAlphaI[i] = newAi[i]
		
		if count == banyakData:
			break
	
	for i in range(len(arrayAlphaI)):
		print("alpha ", (i+1), "= %.3f" %arrayAlphaI[i])

def calculateSign(x):
	result = 0
	for i in range(banyakData):
		temp = (arrayKelas[i] * arrayAlphaI[i] 
		* polinomialDegreeUpToD(arrayData[i], x))
		print("jarak ke %d = %.3f" %((i+1), temp))
		result += temp
	print(result)	
	if result < 0:
		return -1
	else :
		return 1
	
#print(linier( [2], [2] ) )
#setArrayData()
printArrayData()
seqLearning()
print("Sign for (1, 5) = %d" %calculateSign([1, 5]))
#printArrayD()