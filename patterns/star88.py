a=int(input("enter the height of pyramid"))
for i in range(a,0,-1):
    h=(i-1)*2
    print((a-i)*" ",end="")
    print(i,end="")
    print((h-1)*" ",end="")
    if(i>1):
        print(i,end="")       
    print()
        
    
        
       

