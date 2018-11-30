
selectedKernel = 3
degree = 0
constanta = 0
thou = 0
lamda = 0
maksimalLoop = 500 

# Data
# banyak fitur satu baris data, serta sebagai index kelas
banyakFitur = 0  
# banyak semua data
banyakData = 0

arrayData = []

arrayAlphaI = []

def normalisasiData(arrayData, minRange = 0, maxRange = 1):
	maxFiturI = []
	minFiturI = []
	arrayRes = []
	for j in range(banyakFitur):
		maxFiturI.append( max( max([arrayData[i][j:j+1] for i in range(0, banyakData)]) ) )
		minFiturI.append( min( min([arrayData[i][j:j+1] for i in range(0, banyakData)]) ) )
		
	for i in range(banyakData):
		temp = []
		for j in range(banyakFitur):
			temp.append( (minRange +
				( (arrayData[i][j] - minFiturI[j]) * (maxRange - minRange)
				/ ( maxFiturI[j] - minFiturI[j] ) ) ) )
		temp.append(arrayData[i][banyakFitur])
		arrayRes.append(temp)
	return arrayRes
	
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

def setGamma(maxGamma):
	print("Masukkan gamma antara 0 - %.5f" %maxGamma)
	while True:
		gamma = float(input("Input gamma: "))
		if gamma <= 0 and gamma >= maxGamma:
			print("Masukkan gamma lebih dari 0 dan kurang dari %.5f" %maxGamma)
		else:
			break
	return gamma
	
def setSelectedKernel():
	global selectedKernel
	print("1. Linier")
	print("2. Polinomial of Degree D")
	print("3. Polinomial of Degree up to D")
	print("4. Gaussian RBF")
	print("5. Sigmoid")
	print("6. Invers Multi Kuadratik")
	print("7. Additive")
	selectedKernel = int(input("Select Kernel: "))	

def setArrayData():
	global banyakData
	global banyakFitur
	
	arrayData = []
	banyakFitur = int(input("Masukkan banyak fitur: "))
	banyakData = int(input("Masukkan banyak data: "))
	
	print("Silahkan masukkan data setiap baris (dipisahkan dengan spasi)")

	# print kolom fitur dan kelas
	for i in range(banyakFitur):
		print("Fitur", (i+1), end='|')
	print("Kelas / Kategori")
	
	for i in range(banyakData):
		row = [int(x) for x in input().split()]
		arrayData.append(row)
	return arrayData

def printArray(array):
	for i in range(len(array)):
		for j in range(len(array[i])):
			print("%.3f" %array[i][j], end=' ')
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
	for i in range(banyakFitur):
		result += x[i] * y[i]
	result = result + constanta
	result = result ** degree
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
	if lamda == 0:
		setLamda()
		
	arrayD = []
	for i in range(banyakData):
		row = []
		for j in range(banyakData):
			row.append( arrayData[i][banyakFitur] * arrayData[j][banyakFitur] 
			* ( (calculateKernel(arrayData[i], arrayData[j])) + (lamda**2) ) )
		arrayD.append(row)
	return arrayD
	
def findMaxGamma(arrayD):
	return (2 / (max(max(arrayD))))

def seqLearning(treshold):
	global arrayAlphaI
	arrayAlphaI = [0.0 for i in range(banyakData)]
	arrayD = calculateArrayD()
	maxGamma = findMaxGamma(arrayD)
	gamma = setGamma(maxGamma)
	printArray(arrayD)
	
	dAi = [0.0 for i in range(banyakData)]
	newAi = [0.0 for i in range(banyakData)]
	countLoop = 0
	for i in range(maksimalLoop):
		ei = [0.0 for i in range(banyakData)]
		for i in range(banyakData):
			for j in range(banyakData):
				ei[i] += (arrayAlphaI[j] * arrayD[i][j])
			dAi[i] = min( max(gamma * (1 - ei[i]), -1 * arrayAlphaI[i] ), (constanta - arrayAlphaI[i]) )
			newAi[i] = arrayAlphaI[i] + dAi[i]
			
		count = 0
		for i in range(banyakData):
			if dAi[i] <= treshold:
				count += 1
			arrayAlphaI[i] = newAi[i]
		
		if count == banyakData:
			break
		countLoop += 1
	
	print("Melakukan perulangan sebanyak %d kali" %countLoop)
	for i in range(len(arrayAlphaI)):
		print("alpha ", (i+1), "= %.3f" %arrayAlphaI[i])
	print("")

def calculateSign(x):
	result = 0
	for i in range(banyakData):
		temp = (arrayData[i][banyakFitur] * arrayAlphaI[i] 
		* calculateKernel(arrayData[i], x))
		print("jarak ke %d  = %.3f" %((i+1), temp))
		result += temp
	print("total jarak = %.3f" %result)	
	if result < 0:
		return -1
	else :
		return 1

def SVM(dataTraining, dataUji, treshold):
	global arrayData
	global banyakData
	global banyakFitur
	
	banyakFitur = len(dataTraining[0]) - 1
	banyakData = len(dataTraining)
	
	arrayNorm = normalisasiData(dataTraining)
	printArray(arrayNorm)
	arrayData = arrayNorm
	
	seqLearning(treshold)
	return calculateSign(dataUji)
	

arrayData = [
  [60,  165, 1],
  [70,  160, 1],
  [80,  165, 1],
  [100, 155, -1],
  [40,  175, -1]]

dataCari = [90, 155]
	
arrayDataTest = [
  [1,   1, -1],
  [1,  -1,  1],
  [-1,  1,  1],
  [-1, -1, -1]]
  
find = [1, 5]

print("Sign for", find, " = %d" %SVM(arrayData, dataCari, 0.001) )