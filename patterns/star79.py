a=int(input("enter the height of pyramid"))
c="A"
for i in range(0,a):
    print((a-i-1)*" ",end="")
    for j in range(0,i+1):
        print(chr(ord(c)+i)+" ",end="")
    print()
for i in range(1,a):
    print(i*" ",end="")
    for j in range(a,i,-1):
        print(chr(ord(c)+(a-i-1))+" ",end="")
    print()
    
 
