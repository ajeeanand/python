#upper triangle
a=int(input("enter the height of pyramid"))
c="A"
h=1
for i in range(0,a):
    print((a-i-1)*" ",end="")
    print(chr(ord(c)+(a-i)-1),end="")
    print(h*" ",end="")
    if(i>0):
        print(chr(ord(c)+(a-i)-1),end="")
        h=h+2
    print()
#bottom triangle
for i in range(a-1,0,-1):
    h=(i-1)*2
    print((a-i)*" ",end="")
    print(chr(ord(c)+(a-i)),end="")
    print((h-1)*" ",end="")
    if(i>1):
        print(chr(ord(c)+(a-i)),end="")       
    print()
        
    
        
       

