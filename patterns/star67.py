a=int(input("enter the row"))
c="A"
for i in range(0,a):
    print((a-i)*" ",end="")
    for j in range(0,i+1):
        print(chr(ord(c)+i)+" ",end="")
    print()
    
 
