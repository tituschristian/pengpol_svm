## Normalisasi
def normalisasiData(arrayData, minRange = 0, maxRange = 1):
	maxFiturI = []
	minFiturI = []
	arrayRes = []
	banyakData = len(arrayData)
	banyakFitur = len(arrayData[0])
	for j in range(banyakFitur):
		maxFiturI.append( max( max( [arrayData[i][j:j+1] for i in range(banyakData)] ) ) )
		minFiturI.append( min( min( [arrayData[i][j:j+1] for i in range(banyakData)] ) ) )
		
	for i in range(banyakData):
		temp = []
		for j in range(banyakFitur):
			temp.append( (minRange +
				( (arrayData[i][j] - minFiturI[j]) * (maxRange - minRange)
				/ ( maxFiturI[j] - minFiturI[j] ) ) ) )
		arrayRes.append(temp)
	return arrayRes

	
## Kernel
# utils
selectedKernel = 0
def setSelectedKernel():
	global selectedKernel
	print("1. Linier")
	print("2. Polinomial of Degree D")
	print("3. Polinomial of Degree up to D")
	selectedKernel = int(input("Select Kernel: "))
	
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

def linier(x, y):
	result = 0
	for i in range(len(x)):
		result += x[i] * y[i]
	return result
			
def polinomialDegreeD(x, y):
	degree = 2
	result = 0
	
	for i in range(len(x)):
		result += x[i] * y[i]
	result = result ** degree
	return result
	
def polinomialDegreeUpToD(x, y):
	constanta = 1
	degree = 2
	result = 0
	
	for i in range(len(x)):
		result += x[i] * y[i]
	result = result + constanta
	result = result ** degree
	return result
# run
def calculateArrayKernel(data, kelas):
	arrayKernel = []
	for i in range(len(data) - 1):
		row = []
		for j in range(len(data) - 1):
			row.append( calculateKernel(data[i], data[j]) )
		arrayKernel.append(row)
	return arrayKernel


## sequential learning
# utils
def findMaxGamma(arrayD):
	return (2 / (max(max(arrayD))))

def setGamma(maxGamma):
	print("Masukkan gamma antara 0 - %.5f" %maxGamma)
	while True:
		gamma = float(input("Input gamma: "))
		if gamma <= 0 and gamma >= maxGamma:
			print("Masukkan gamma lebih dari 0 dan kurang dari %.5f" %maxGamma)
		else:
			break
	return gamma
# utils step 1
def calculateArrayD(arrayKernel, kelas):
	lamda = 3
	arrayD = []
	banyakData = len(arrayKernel)
	
	for i in range(banyakData):
		row = []
		for j in range(banyakData):
			row.append( kelas[i] * kelas[j] * 
			( arrayKernel[i][j] + (lamda**2) ) )
		arrayD.append(row)
	return arrayD


## Sequential
# utils
def printArray(array):
	for i in range(len(array)):
		for j in range(len(array[i])):
			print("%.3f" %array[i][j], end=' ')
		print("")
	print("")
# run
def sequentialLearning(arrKernel, kelas):
	constanta = 1
	gamma = 0
	maksimalLoop = 1000
	treshold = 0.00001
	banyakData = len(arrKernel)
	
	# Step 1
	arrayD = calculateArrayD(arrKernel, kelas)

	# Step 2
	maxGamma = findMaxGamma(arrayD)
	gamma = setGamma(maxGamma)
	Ai = [0.0 for i in range(banyakData)]
	deltaAi = [0.0 for i in range(banyakData)]
	newAi = [0.0 for i in range(banyakData)]
	countLoop = 0
	for i in range(maksimalLoop):
		Ei = [0.0 for i in range(banyakData)]
		for j in range(banyakData):
			for k in range(banyakData):
				Ei[j] += (Ai[j] * arrayD[j][k])	
			deltaAi[j] = min( max(gamma * (1 - Ei[j]), - 1 * Ai[j] ), (constanta - Ai[j]) )
			newAi[j] = Ai[j] + deltaAi[j]
		
		# Step 3
		count = 0
		for z in range(banyakData):
			if deltaAi[z] <= treshold:
				count += 1
			Ai[z] = newAi[z]
		
		if count == banyakData:
			break
		countLoop += 1
	
	print("Melakukan perulangan sebanyak %d kali" %countLoop)
	
	## print array alpha
	for i in range(len(Ai)):
		print("alpha ", (i+1), "= %.3f" %Ai[i])
	print("")
	
	return Ai
	
## hitung nilai jarak data baru
def calculateSign(alpha, data, kelas):
	result = 0
	banyakData = len(data) - 1
	dataBaru = data[-1]
	for i in range(banyakData):
		temp = (kelas[i] * alpha[i] 
		* calculateKernel(data[i], dataBaru))
		#print("jarak ke %d  = %.3f" %((i+1), temp))
		result += temp
	return result
	
## MAIN
def SVM():
	arrayData = [
	  [60,  165],
	  [70,  160],
	  [80,  165],
	  [100, 155],
	  [40,  175],
	  [90,  155]]
	  
	arrayKelas = [
		1,
		1,
		1,
		-1,
		-1]
	'''
	arrayData = [
	  [1,  1],
	  [1,  -1],
	  [-1,  1],
	  [-1, -1],
	  [1 , 5]]
	  
	arrayKelas = [
		-1,
		1,
		1,
		-1]
	'''
	## normalisasi data
	arrayData = normalisasiData(arrayData, 1, 2)
	printArray(arrayData)
	
	## hitung array kernel
	arrayKernel = calculateArrayKernel(arrayData, arrayKelas)
	printArray(arrayKernel)
	
	## sequential learning
	arrayAlpha = sequentialLearning(arrayKernel, arrayKelas)
	
	## hitung alpha i * (kernel data baru dengan data training)
	dataBaru = arrayData[-1]
	result = calculateSign(arrayAlpha, arrayData, arrayKelas)
	print("total jarak = %.3f" %result)	
	kategori = 1 if result > 0 else -1
	print("kategori", kategori)
	
SVM()
