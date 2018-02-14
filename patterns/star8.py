a=int(input("enter the row"))
b=int(input("enter the coloumn"))
c="A"
for i in range(b-1,-1,-1):
    for j in range(a,0,-1):
        print(chr(ord(c)+i),end=" ")
    print()

