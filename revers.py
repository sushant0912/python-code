n=int(input("Enter the number:"))
n1=n
revers=0
# while n>0:
#     rem=n%10
#     n=n//10
#     revers=revers*10+rem
for i in range(len(str(n))):
    rem=n%10
    n=n//10
    revers=rem+revers*10
print(f"revers of {n1} is {revers}")