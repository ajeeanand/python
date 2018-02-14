a=int(input("enter the row"))
for i in range(0,a):
    print((a-i)*" ",end="")
    for j in range(0,i+1):
        print(str(j+1)+" ",end="")
    print()
    
 
