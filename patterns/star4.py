a=int(input("enter the row"))
b=int(input("enter the coloumn"))
c='A'
for i in range(0,b):
    for j in range(0,a):
        print(chr(ord(c)+i),end=" ")
    print()

