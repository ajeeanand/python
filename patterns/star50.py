a=int(input("enter the row"))
h=a+(a-1)
for i in range(1,a+1):
    print(i*" ",end="")
    for j in range(h-1,-1,-1):
        print(h-j,end="")
    h=h-2
    print()
    
