a=int(input("enter the height of pyramid"))
c="A"
h=1
for i in range(0,a):
    print((a-i)*" ",end="")
    print(chr(ord(c)+i),end="")
    print(h*" ",end="")
    if(i>0):
        print(chr(ord(c)+i),end="")
        h=h+2
    print()
        
    
        
       

