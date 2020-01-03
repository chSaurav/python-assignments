def Reverse(list):
    new_lst=[]
    new_lst = list[::-1]
    print(new_lst)

#driverCode
list = []
for i in range(10):
    val=int(input("Enter Number"))
    list.append(val)
Reverse(list)
