def top():
    s=3
    for i in range(1,5):
        for k in range(1, s+1):
            print(end=" ")
        print("<>",("...."*(i-1)),"<>")
        s=s-1
def bottom():
    s=1
    for i in range(4,0,-1):
        for k in range(0,s-1):
            print(end=" ")
        print("<>",("...."*(i-1)),"<>")
        s=s+1
top()
bottom()
