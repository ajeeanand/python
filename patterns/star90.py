a=int(input("enter the height of pyramid"))
c="A"
for i in range(a,0,-1):
    h=(i-1)*2
    print((a-i)*" ",end="")
    print(chr(ord(c)+i-1),end="")
    print((h-1)*" ",end="")
    if(i>1):
        print(chr(ord(c)+i-1),end="")       
    print()
        
    
        
       

