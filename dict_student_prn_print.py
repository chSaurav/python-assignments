file = open("prn2.txt")
l={}
f=[]
for line in file:
    k = line.split(' ')
    f.append(int(k[0]))
    l[int(k[0])] = k[1]
f.sort()
for i in range(0,len(f)):
    print(f[i],l[f[i]])
