a=int(input("enter the row"))
c=ord("A")+a
for i in range(0,a):
    for j in range(a,i,-1):
        print(chr((c-i)-1),end=" ")
    print()
