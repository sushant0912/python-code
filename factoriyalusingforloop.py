print('------------factortail number------------')
n = int(input("Enter a number:"))
fact= float(1)
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of {n} = {fact}")