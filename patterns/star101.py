#upper part
a=int(input("enter the row"))
h=a*2
for i in range(1,a+1):
    h=h-1
    print(h*" ",end="")
    for j in range(0,i):
        print("* ",end="")
    print()
#lower part
h=1
for i in range(1,a+1):
    print((a-i)*" ",end="")
    print(i*"* ",end="")
    print(((a-i)*2)*" ",end="")
    print(i*"* ")
    h=h+2
    
        
        

        
    
        
       

