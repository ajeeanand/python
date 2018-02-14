a=int(input("enter the row"))
h=1
for i in range(a,0,-1):
    print(i*" ",end="")
    for j in range(0,h):
        print(j+1,end="")
    h=h+2
    print()
