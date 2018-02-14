a=int(input("enter the row"))
c="A"
for i in range(a,0,-1):
    print((a-i)*" ",end="")
    for j in range(0,i):
        print(chr(ord(c)+i-1)+" ",end="")
    print()
    
 
