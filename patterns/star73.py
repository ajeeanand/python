a=int(input("enter the row"))
c="A"
for i in range(a,0,-1):
    print((a-i)*" ",end="")
    for j in range(i,0,-1):
        print(chr(ord(c)+j-1)+" ",end="")
    print()
    
 
