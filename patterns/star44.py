a=int(input("Enter the number"))
res="A"
for i in range(1,a+1):
    print((a-i)*" ",end="")
    print(res)
    res=chr(65+i)+res+chr(65+i)
