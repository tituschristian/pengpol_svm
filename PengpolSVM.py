
selectedKernel = 0
degree = 0
constanta = 0
thou = 0
lamda = 0
gamma = 0
maxGamma = 0
maksimalLoop = 100

# Data
banyakFitur = 0
banyakData = 0

arrayData = []
'''
arrayData = [
  [60,  165],
  [70,  160],
  [80,  165],
  [100, 155],
  [40,  175],
  [90, 	155]]
'''

'''
arrayKelas = [
  1, 1, 1, -1, -1
]
'''

arrayAlphaI = []
arrayD = []
arrayK = []

def normalisasiData(minRange = 0, maxRange = 1):
	global arrayData
	maxFiturI = []
	minFiturI = []
	arrayRes = []
	for j in range(banyakFitur):
		maxFiturI.append( max(max([arrayData[i][j:j+1] for i in range(0, banyakData)])) )
		minFiturI.append( min(min([arrayData[i][j:j+1] for i in range(0, banyakData)])) )
	
	for i in range(banyakData + 1):
		temp = []
		for j in range(banyakFitur):
			temp.append( (minRange +
				( (arrayData[i][j] - minFiturI[j]) * (maxRange - minRange)
				/ ( maxFiturI[j] - minFiturI[j] ) ) ) )
		#print(temp)
		arrayRes.append(temp)
	return arrayRes
	#print("max ", maxFiturI)
	#print("min ", minFiturI)
	#print(arrayRes)
	
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
	
def setSelectedKernel():
	print("1. Linier")
	print("2. Polinomial of Degree D")
	print("3. Polinomial of Degree up to D")
	print("4. Gaussian RBF")
	print("5. Sigmoid")
	print("6. Invers Multi Kuadratik")
	print("7. Additive")
	selectedKernel = input("Select Kernel: ")	

def setArrayData(dataInput = []):
	global arrayData
	global banyakData
	global banyakFitur
	if banyakFitur == 0:
		banyakFitur = int(input("Masukkan banyak fitur: "))
	if banyakData == 0:
		banyakData = int(input("Masukkan banyak data: "))
	
	if len(dataInput) == 0:
		print("Silahkan masukkan data setiap baris")

		for i in range(banyakFitur):
			print("Fitur", (i+1), end='|')

		print("Kelas / Kategori")
		for i in range(banyakData):
			row = [int(x) for x in input().split()]
			arrayData.append(row)
	else :
		arrayData = dataInput
		
def printArrayData():
	for i in range(banyakData):
		for j in range(banyakFitur):
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
		print(result, "->", end='')
	result = result + constanta
	print("result plus constanta", result)
	result = result ** degree
	print("result ", result)
	return result

def calculateKernel(x, y):
	if selectedKernel == 0 :
		print("Please select kernel")
		setSelectedKernel()
	
	if selectedKernel == 1:
		return linier(x, y)
	elif selectedKernel == 2:
		return polinomialDegreeD(x, y)
	elif selectedKernel == 3:
		return polinomialDegreeUpToD(x, y)

def calculateArrayD():
	global arrayD
	global maxGamma
	for i in range(banyakData):
		row = []
		for j in range(banyakData):
			print("data yang digunakan ", arrayData[i], "dan ", arrayData[j])
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
	for i in range(maksimalLoop):
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
		
		print("cek")
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

arrayDataTest = [
  [1,   1, -1],
  [1,  -1,  1],
  [-1,  1,  1],
  [-1, -1, -1]]
  
banyakData = 4
banyakFitur = 2
setArrayData(arrayDataTest) 
printArrayData()
'''
arrayKelas = [
  -1, 1, 1, -1
]
'''
'''
arrayData = normalisasiData()
print(arrayData)
printArrayData()
seqLearning()
print("Sign for (90, 155) = %d" %calculateSign([90, 155]))
'''
#print("Sign for (1, 5) = %d" %calculateSign([1, 5]))
#printArrayD()