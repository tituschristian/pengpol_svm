
selectedKernel = 0

def linier(x, y):
	result = x.copy()
	for i in range(len(x)):
		result[i] = x[i] * y[i]
	return result
			
def polinomialDegreeD(x, y):
	result = x.copy()
	for i in range(len(x)):
		result[i] = x[i] * y[i]
	return result
	
def polinomialDegreeUpToD(x, y):
	result = x.copy()
	for i in range(len(x)):
		result[i] = x[i] * y[i]
	return result

def setSelectedKernel():
	print("1. Linier")
	print("2. Polinomial of Degree D")
	print("3. Polinomial of Degree up to D")
	print("4. Gaussian RBF")
	print("5. Sigmoid")
	print("6. Invers Multi Kuadratik")
	print("7. Additive")
	selectedKernel = input("Select Kernel: ")

'''def calculateKernel()
	if (selectedKernel == 0):
		print("Please select kernel")
		setSelectedKernel()
	else:
'''		

def seqLearning():
	ai = 0
	a = 0
	return 0
	
print(linier( [2], [2] ) )