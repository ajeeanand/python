a=int(input("enter the height of pyramid"))
c="A"
for i in range(0,a):
    print((a-i-1)*" ",end="")
    for j in range(0,i+1):
        print(chr(ord(c)+j)+" ",end="")
    print()
for i in range(0,a+1):
    print((i+1)*" ",end="")
    for j in range(i+1,a):
        print(chr(ord(c)+j)+" ",end="")
    print()
    
 
