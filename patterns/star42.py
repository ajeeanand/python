a=int(input("enter the row"))
c="A"
h=0
for i in range(a,0,-1):
    print(i*" ",end="")
    for j in range(0,h+1):
        print(chr(ord(c)+h-j),end="")
    h=h+2
    print()
