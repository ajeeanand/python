a=int(input("enter the row"))
h=a+(a-1)
for i in range(1,a+1):
    print(i*" ",end="")
    for i in range(0,h):
        print("*",end="")
    h=h-2
    print()
    
