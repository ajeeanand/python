a=int(input("enter the row"))
for i in range(0,a):
    print(((a-i)-1)*" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()
