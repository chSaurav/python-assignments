#creation of revnum function
def revnum(num):
    newarr = []
    for i in range(len(num)):
        newarr[0+i] = num[len(num) - i]
    print(newarr)

#driverCode
num = []
for i in range(10):
    value = int(input("Enter Number : "))
num.append(value)

#reverseNumber -- > function call

revnum(num)
