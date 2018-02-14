a=int(input("enter the row"))
for i in range(a,0,-1):
    print(((a-i))*" ",end="")
    for j in range(i,0,-1):
        print(i,end="")
    print()
