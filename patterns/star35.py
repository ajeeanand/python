a=int(input("enter the row"))
c=a+1
h=1
for i in range(a,0,-1):
    print(i*" ",end="")
    for j in range(0,h):
        print(c-i,end="")
    h=h+2
    print()
