a=int(input("enter the row"))
c="A"
h=a+(a-1)
for i in range(a-1,-1,-1):
    print((a-i-1)*" ",end="")
    for j in range(0,h):
        print(chr(ord(c)+h-1),end="")
    h=h-2
    print()
    
