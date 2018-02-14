from math import *
a=int(input("enter the row"))
c="A"
for i in range(a,-(a+1),-1):
    print(abs(i)*" ",end="")
    for j in range(a,abs(i)-1,-1):
        print(chr(ord(c)+j),end="")
    print()
    
 
