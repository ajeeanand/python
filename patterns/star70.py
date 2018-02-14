a=int(input("enter the row"))
for i in range(a,0,-1):
    print((a-i)*" ",end="")
    for j in range(0,i):
        print(str(i)+" ",end="")
    print()
    
 
