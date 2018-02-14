a=int(input("enter the row"))
for i in range(0,a):
    print(i*" ",end="")
    for j in range(a,i,-1):
        print(a-j+1,end="")
    print()
