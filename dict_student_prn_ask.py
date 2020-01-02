file = open("prn2.txt","w")
n = int(input("Number of Names : "))
for i in range(0,n):
    prn = input("Enter PRN : ")
    name = input("Enter Name : ")
    file.write(prn + " "+name+" \n")
file.close()
