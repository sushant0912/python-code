n=int(input("enter a number:"))
i=1
a=0
b=1
for i in range(1,n-1):
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1