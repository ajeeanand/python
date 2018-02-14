a=int(input("enter the height of pyramid"))
h=1
for i in range(0,a):
    print((a-i)*" ",end="")
    print((a-i),end="")
    print(h*" ",end="")
    if(i>0):
        print((a-i),end="")
        h=h+2
    print()
        
    
        
       
