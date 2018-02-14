a=int(input("Enter the number"))
res="0"
for i in range(1,a):
    print((a-i-1)*" ",end="")
    print(res)
    res=str(i)+res+str(i)
