a=int(input("enter the row"))

for i in range(0,a):
    c=a-1
    for j in range(a,i,-1):
        print(a-c,end=" ")
        c-=1
    print()
