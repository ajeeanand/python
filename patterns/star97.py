a=int(input("enter the row"))
h=a+(a-2)
for i in range(0,a):
    print((i+1)*"*",end="")
    if(i<a):
        print((h)*" ",end="")
        h=h-2
    print((i+1)*"*",end="")
    print()
        

        
    
        
       

