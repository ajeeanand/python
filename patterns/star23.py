a=int(input("enter the row"))
c="A"
for i in range(0,a):
    for j in range(a,i,-1):
        print(chr(ord(c)+j-1),end=" ")
    print()
