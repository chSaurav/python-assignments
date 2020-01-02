#function
def ascsort(arr):
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if(arr[i] > arr[j]):
				temp = arr[i]
				arr[i] = arr[j]
				inum[j] = temp
	#displaying elements in ascending order
	for i in range(len(arr)):
		print(arr[i])

#driverCode
arr = []
for i in range(0,10):
	num = int(input("Enter No : "))
	arr.append(num)
ascsort(arr)
