# break=terminates loop

for i in range(1, 6):
    if i ==3:
        print(i)
        break
    print("work stopped ")
else:
    print(i)

print("work completed")

# pass-pass from next iteration also execute next step 

for i in range(1, 6):
    if i == 3:
        # print(i)
        pass
       print(i)
    print("work stopped")
else:
    print(i)

print("work completed")

for i in range(5):
    pass

# While loop

while True:
    n = int(input("enter number="))
    if n == 11:
        print("keep trying")
i = 1
while i <= 5:
    print(i)
    if i == 3:
        # 