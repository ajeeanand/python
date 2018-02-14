#upper triangle
a=int(input("enter the height of pyramid"))
h=1
for i in range(1,a+1):
    print((a-i)*" ",end="")
    print("*",end="")
    print(h*" ",end="")
    if(i>1):
        print("*",end="")
        h=h+2
    print()
#bottom triangle
for i in range(a-1,0,-1):
    h=(i-1)*2
    print((a-i)*" ",end="")
    print("*",end="")
    print((h-1)*" ",end="")
    if(i>1):
        print("*",end="")       
    print()
        
    
        
       

