a=int(input("enter the height of pyramid"))
for i in range(0,a):
    print((a-i-1)*" ",end="")
    for j in range(0,i+1):
        print(str(j+1)+" ",end="")
    print()
for i in range(1,a):
    print(i*" ",end="")
    for j in range(i,a):
        print(str(j+1)+" ",end="")
    print()
    
 
