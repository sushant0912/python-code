msg="welcome to python world"
# for i in msg:
#    print(i)
msg =["welcome to python world"]
for i in msg :
    if i == "e":
        break
    else:
        print(i)
# write a program to print a factorial no from 1 to 10
try:
    n= int(input("enter n="))
    # fact = 1
    # for i in range(1, n + 1):
    #    fact = fact * i
    # print(f" factorial of {n}={fact}")

    n1 = n
    rev = 0
    for i in range(len(str(n))):
        rem = n % 10
        n = n // 10
        rev = rev * 10 + rem
    print(f"Reverse of {n1}={rev}")
except:
    print("invalid input")