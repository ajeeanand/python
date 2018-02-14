from math import *
a=int(input("enter the row"))
for i in range(a,-(a+1),-1):
    print(abs(i)*" ",end="")
    for j in range(a,abs(i)-1,-1):
        print(j,end="")
    print()
    
 
